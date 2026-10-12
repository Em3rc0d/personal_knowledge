#!/usr/bin/env python3
"""REC-012 bounded offline baseline. Python stdlib only.

This is an intentionally deterministic *agent topology* fixture. It does NOT
contain an LLM or produce evidence of real-model multi-agent superiority.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import platform
import statistics
import sys
import time
from typing import Any

HERE = Path(__file__).resolve().parent
KNOWN = {
    'DATA_EXFIL': 'security', 'AUTH_BYPASS': 'security',
    'CONNECTION_POOL': 'database', 'QUERY_TIMEOUT': 'database',
    'UI_CRASH': 'frontend', 'STYLE_GLITCH': 'frontend',
    'PAYMENT_FAIL': 'payments', 'WEBHOOK_DELAY': 'integrations',
}
PRIORITY = ('DATA_EXFIL','AUTH_BYPASS','CONNECTION_POOL','QUERY_TIMEOUT','PAYMENT_FAIL','UI_CRASH','WEBHOOK_DELAY','STYLE_GLITCH')

@dataclass(frozen=True)
class Run:
    status: str
    category: str | None
    team: str | None
    severity: str | None
    tool_calls: int
    handoffs: int
    error: str | None = None

    def output(self) -> dict[str,str | None]:
        return {'category':self.category, 'team':self.team, 'severity':self.severity}

class ValidationError(Exception):
    pass

def analyze_logs(ticket: dict[str, Any], fault: str | None = None) -> dict[str,str]:
    if fault == 'raise':
        raise RuntimeError('injected-log-tool-failure')
    if fault == 'stall':
        time.sleep(0.025)  # Explicit fault injection only; never in nominal benchmark.
    events = ticket['logs']
    category = next((code for code in PRIORITY if code in events), 'UNKNOWN')
    result = {'category':category,'team':KNOWN.get(category,'unassigned')}
    if fault == 'malformed':
        return {'category':category}  # deliberately missing team
    return result

def analyze_impact(ticket: dict[str, Any], fault: str | None = None) -> dict[str,Any]:
    if fault == 'raise':
        raise RuntimeError('injected-impact-tool-failure')
    if fault == 'stall':
        time.sleep(0.025)
    inp = ticket['impact']
    result = {'users':inp['users'], 'production':inp['production'], 'sensitive':inp['sensitive']}
    if fault == 'malformed':
        return {'users':'INVALID', 'production':inp['production'], 'sensitive':inp['sensitive']}
    return result

def merge(log: dict[str,Any], impact: dict[str,Any]) -> tuple[str,str,str]:
    if set(log) != {'category','team'} or set(impact) != {'users','production','sensitive'}:
        raise ValidationError('invalid-handoff-fields')
    cat, team = log['category'], log['team']
    if cat not in {*KNOWN.keys(),'UNKNOWN'} or team != KNOWN.get(cat,'unassigned'):
        raise ValidationError('invalid-log-handoff')
    users, prod, sensitive = impact['users'], impact['production'], impact['sensitive']
    if type(users) is not int or users < 0 or type(prod) is not bool or type(sensitive) is not bool:
        raise ValidationError('invalid-impact-handoff')
    sev = ('critical' if cat in ('DATA_EXFIL','AUTH_BYPASS') and sensitive
           else 'high' if cat in ('CONNECTION_POOL','QUERY_TIMEOUT','PAYMENT_FAIL') and users >= 100 and prod
           else 'medium' if prod and users > 0 else 'low')
    return cat, team, sev

def fail(code:str, tools:int, handoffs:int) -> Run:
    return Run('failed',None,None,None,tools,handoffs,code)

def single_actor(ticket:dict[str,Any], fault:tuple[str,str]|None=None, timeout_s:float=.010)->Run:
    """One deterministic policy actor, two tool observations, one synthesis."""
    started=time.perf_counter()
    fc, action = fault or (None,None)
    calls=0
    try:
        calls+=1
        log=analyze_logs(ticket, action if fc=='logs' else None)
        if time.perf_counter()-started > timeout_s:
            return fail('time-budget-exceeded',calls,0)
        calls+=1
        impact=analyze_impact(ticket,action if fc=='impact' else None)
        if time.perf_counter()-started > timeout_s:
            return fail('time-budget-exceeded',calls,0)
        cat,team,sev=merge(log,impact)
        return Run('completed',cat,team,sev,calls,0)
    except (ValidationError,RuntimeError) as exc:
        return fail(str(exc),calls,0)

def manager_workers(ticket:dict[str,Any], fault:tuple[str,str]|None=None, timeout_s:float=.010)->Run:
    """Manager + two independent specialist policy actors and explicit handoffs."""
    fc, action = fault or (None,None)
    started=time.perf_counter()
    # Real worker threads; timeout is cooperative for in-flight work. The pool's
    # shutdown wait may exceed requested deadline. This is *not* hard cancellation.
    executor=ThreadPoolExecutor(max_workers=2)
    calls=2
    handoffs=0
    try:
        lf=executor.submit(analyze_logs,ticket,action if fc=='logs' else None)
        imf=executor.submit(analyze_impact,ticket,action if fc=='impact' else None)
        try:
            log=lf.result(timeout=max(0,timeout_s-(time.perf_counter()-started)))
            handoffs+=1
            impact=imf.result(timeout=max(0,timeout_s-(time.perf_counter()-started)))
            handoffs+=1
        except TimeoutError:
            lf.cancel();imf.cancel()
            return fail('time-budget-exceeded',calls,handoffs)
        if time.perf_counter()-started > timeout_s:
            return fail('time-budget-exceeded',calls,handoffs)
        cat,team,sev=merge(log,impact)
        return Run('completed',cat,team,sev,calls,handoffs)
    except (ValidationError,RuntimeError) as exc:
        return fail(str(exc),calls,handoffs)
    finally:
        executor.shutdown(wait=True,cancel_futures=True)

def load_fixtures(path:Path)->list[dict[str,Any]]:
    fixtures=json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(fixtures,list) or len(fixtures)<8:
        raise ValueError('fixture set too small')
    if len(set(t['id'] for t in fixtures))!=len(fixtures):
        raise ValueError('duplicate task IDs')
    return fixtures

def quant(vals:list[float], frac:float)->float:
    return sorted(vals)[max(0,min(len(vals)-1,int(len(vals)*frac+0.999999)-1))]

def bench(fixtures:list[dict[str,Any]], trials:int, timeout_s:float, fixture_hash:str) -> dict[str,Any]:
    durations={'single':[],'multi':[]}
    per={'single':[],'multi':[]}
    runs={'single':[],'multi':[]}
    for repeat in range(trials):
        # Alternate order to reduce warm-up/order bias; tasks deterministic.
        for t in fixtures:
            order=[('single',single_actor),('multi',manager_workers)]
            if (repeat + len(t['id'])) % 2: order.reverse()
            for label,fn in order:
                start=time.perf_counter_ns()
                result=fn(t,timeout_s=timeout_s)
                elapsed=(time.perf_counter_ns()-start)/1e6
                durations[label].append(elapsed)
                passes=result.status=='completed' and result.output()==t['expected']
                per[label].append({'task_id':t['id'],'success':passes,'status':result.status,'error':result.error,'elapsed_ms':round(elapsed,6),'tool_calls':result.tool_calls,'handoffs':result.handoffs})
                runs[label].append(result)
    summary={}
    for label in ('single','multi'):
        durations_ms=durations[label]
        summary[label]={
            'n':len(durations_ms),
            'outcome_correct':sum(r['success'] for r in per[label]),
            'outcome_incorrect':sum(not r['success'] for r in per[label]),
            'median_ms':round(statistics.median(durations_ms),6),
            'p95_ms':round(quant(durations_ms,.95),6),
            'total_wall_ms':round(sum(durations_ms),6),
            'total_tool_calls':sum(x.tool_calls for x in runs[label]),
            'total_handoffs':sum(x.handoffs for x in runs[label]),
            'model_calls':0, 'model_tokens':'NOT_APPLICABLE', 'model_cost_usd':'NOT_APPLICABLE',
            'external_api_calls':0,
        }
    fault_cases=[('logs','raise'),('impact','raise'),('logs','malformed'),('impact','malformed'),('logs','stall'),('impact','stall')]
    fault_receipts=[]
    for t in fixtures[:1]:
        for fault in fault_cases:
            row={'fault':':'.join(fault)}
            for label,fn in [('single',single_actor),('multi',manager_workers)]:
                st=time.perf_counter_ns();r=fn(t,fault=fault,timeout_s=timeout_s)
                row[label]={'status':r.status,'error':r.error,'handoffs':r.handoffs,'elapsed_ms':round((time.perf_counter_ns()-st)/1e6,6)}
            fault_receipts.append(row)
    return {
        'experiment':'REC-012-offline-rule-based-topology-v1',
        'evidence_class':'EXECUTED_LOCAL_DETERMINISTIC_FIXTURE_NOT_LLM_BENCHMARK',
        'date_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
        'environment':{'python':sys.version.split()[0],'os':platform.platform(),'cpu_count':'NOT_RECORDED'},
        'task_count':len(fixtures),'repeats_per_task':trials,'fixture_sha256':fixture_hash,
        'predeclared_hypothesis':'Manager+specialists may parallelize independent observations, but orchestration overhead can dominate trivial CPU-fast tasks.',
        'parity':{'same_input':True,'same_two_tools':True,'same_synthesis':True,'same_expected_labels':True,'same_timeout_seconds':timeout_s,'same_model':'NONE (deterministic policy actors)'},
        'topology':{'single':'one policy actor; sequential tool observation','multi':'one manager plus two independent specialist policy actors; parallel observations via 2 threads, typed handoffs; manager owns termination'},
        'nominal':summary,'failures':fault_receipts,
        'limitations':['Synthetic task fixtures; hand-labelled expected results','No LLM, API or stochastic planning; cannot establish LLM multi-agent benefit','Short no-network tools; measured latency is specific to local Python thread startup and scheduler','In-flight threads cannot be forcibly cancelled; deadline may be exceeded before cleanup','No independent task quality assessment outside fixture expectation','Only one host and one benchmark workload; no production certification']
    }

def main()->None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--fixtures',default=str(HERE/'fixtures.json'))
    parser.add_argument('--output',default=str(HERE/'results.json'))
    parser.add_argument('--trials',type=int,default=30)
    parser.add_argument('--timeout-ms',type=float,default=10.)
    args=parser.parse_args()
    if args.trials<1 or args.timeout_ms<=0:parser.error('positive trials and timeout required')
    fixture_path=Path(args.fixtures)
    raw=fixture_path.read_bytes()
    res=bench(load_fixtures(fixture_path),args.trials,args.timeout_ms/1000,hashlib.sha256(raw).hexdigest())
    Path(args.output).write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'nominal':res['nominal'],'failures':[{'fault':x['fault'],'single':x['single']['error'],'multi':x['multi']['error']} for x in res['failures']]},indent=2))
if __name__=='__main__': main()
