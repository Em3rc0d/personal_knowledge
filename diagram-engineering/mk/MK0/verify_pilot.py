#!/usr/bin/env python3
"""Static structural audit. No network and no third-party libraries."""
from pathlib import Path
from html.parser import HTMLParser
import json
import sys

BASE=Path(__file__).resolve().parent/"outputs"
class Audit(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.nodes=[]; self.edges=[]; self.svg=[]; self.bad=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if "id" in a: self.ids.append(a["id"])
        if tag=="svg": self.svg.append(a)
        if "data-node" in a: self.nodes.append(a["data-node"])
        if "data-from" in a: self.edges.append((a.get("data-from"),a.get("data-to")))
        if tag in ("script","iframe","object","embed","foreignobject"): self.bad.append(tag)
        if any(a.get(k,"").startswith(("https://","http://","javascript:","//")) for k in ("href","src","xlink:href")): self.bad.append("remote URL")

def audit(case):
    raw=(BASE/(case+".html")).read_text(encoding="utf-8")
    p=Audit();p.feed(raw)
    errors=[]
    if len(p.svg)!=1: errors.append("svg count")
    if len(p.ids)!=len(set(p.ids)): errors.append("duplicate ids")
    if len(p.nodes)!=len(set(p.nodes)): errors.append("duplicate nodes")
    if p.bad: errors.append("remote or executable content")
    if not p.svg or p.svg[0].get("role")!="img": errors.append("missing role=img")
    refs=p.svg[0].get("aria-labelledby","").split() if p.svg else []
    if len(refs)!=2 or any(k not in p.ids for k in refs): errors.append("missing title+desc IDs")
    if any(a not in p.nodes or b not in p.nodes for a,b in p.edges): errors.append("unresolved endpoints")
    for flag in ('viewBox="0 0 1280 720"','overflow-x:auto','min-width:1280px','data-source-revision='):
        if flag not in raw: errors.append("missing: "+flag)
    return {"case":case,"nodes":len(p.nodes),"edges":len(p.edges),"status":"FAIL" if errors else "PASS","errors":errors}
if __name__=="__main__":
    result=[audit(case) for case in ("echo","ninfa","knowledge")]
    print(json.dumps(result,indent=2))
    sys.exit(1 if any(x["status"]=="FAIL" for x in result) else 0)
