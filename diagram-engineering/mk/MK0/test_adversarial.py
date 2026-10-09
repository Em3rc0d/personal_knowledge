#!/usr/bin/env python3
from pathlib import Path
import json,re,tempfile
from verify_pilot import audit
root=Path(__file__).resolve().parent
spec=json.loads((root/"graph_contract.json").read_text("utf-8"))["echo"]
base=(root/"outputs"/"echo.html").read_text("utf-8")
mutations={
 "svg_onload":lambda x:x.replace('role="img"','role="img" onload="alert(1)"',1),
 "css_import":lambda x:x.replace("<style>","<style>@import url(https://evil.example/a.css);",1),
 "empty_edge":lambda x:x.replace('d="M612 338 H548"','d=""',1),
 "stale_sha":lambda x:x.replace(spec["source_sha"],"0"*40,1),
 "empty_title":lambda x:re.sub(r'(<title id="echo-title">).*?(</title>)',r'\1\2',x,count=1),
 "missing_return":lambda x:x.replace('data-edge="e7"','data-edge="removed"',1),
 "bad_endpoint":lambda x:x.replace('data-to="scheduler"','data-to="ghost"',1),
 "diagonal":lambda x:x.replace('d="M264 198 H328"','d="M264 198 L328 199"',1),
 "remote_href":lambda x:x.replace("<svg xmlns=",'<a href="https://evil.example">x</a><svg xmlns=',1),
 "no_alternative":lambda x:x.replace("<details open>","<div>",1).replace("</details>","</div>",1),
 "poor_contrast":lambda x:x.replace("--muted:#405766","--muted:#b3bcc3",1),
 "missing_text_relation":lambda x:x.replace("<li>InferenceScheduler → ModelRunner — INFERENCE REQUEST</li>","",1),
}
with tempfile.TemporaryDirectory() as directory:
 for name,fn in mutations.items():
  modified=fn(base)
  assert modified!=base,"mutation not applied: "+name
  path=Path(directory)/(name+".html");path.write_text(modified,"utf-8")
  result=audit(path,spec)
  assert result["status"]=="FAIL","undetected: "+name
  print("DETECTED",name)
print("PASS",len(mutations),"/",len(mutations),"negative cases")
