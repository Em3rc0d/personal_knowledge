#!/usr/bin/env python3
"""Offline SVG contracts: no source-semantic certification."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from xml.etree import ElementTree as ET
class Doc(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=[];self.errors=[];self.styles=[];self.instyle=False;self.inlist=False;self.nrels=0;self.ndetails=0;self.nframes=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get("id"):self.ids.append(a["id"])
  if tag in ("script","iframe","object","embed","foreignobject","link","base"):self.errors.append("unsafe tag "+tag)
  if tag=="style":self.instyle=True
  if tag=="ol":self.inlist=True
  if tag=="li" and self.inlist:self.nrels+=1
  if tag=="details":self.ndetails+=1
  if tag=="div" and "frame" in a.get("class","").split():
   self.nframes+=1
   if a.get("tabindex")!="0":self.errors.append("scroll not focusable")
  for k,v in attrs:
   v=v or ""
   if k.startswith("on"):self.errors.append("unsafe handler "+k)
   if k in ("href","src","srcset","xlink:href","action","formaction") and not v.startswith("#"):self.errors.append("unsafe URL "+k)
 def handle_endtag(self,tag):
  if tag=="style":self.instyle=False
  if tag=="ol":self.inlist=False
 def handle_data(self,t):
  if self.instyle:self.styles.append(t)
NUM=r"-?(?:\d+(?:\.\d*)?|\.\d+)(?:e[+-]?\d+)?"
def poly(d):
 if re.sub("[MLHVZmlhvz]|"+NUM,"",d,flags=re.I).strip():raise ValueError("unknown SVG path grammar")
 toks=re.findall("[MLHVZmlhvz]|"+NUM,d,flags=re.I);i=0;x=y=0.;cmd=None;pts=[]
 while i<len(toks):
  v=toks[i]
  if v.isalpha():
   if v.islower() or v=="Z":raise ValueError("relative/closed path")
   cmd=v;i+=1;continue
  if cmd in ("M","L"):
   if i+1>=len(toks) or toks[i+1].isalpha():raise ValueError("missing Y")
   x=float(v);y=float(toks[i+1]);i+=2
  elif cmd=="H":x=float(v);i+=1
  elif cmd=="V":y=float(v);i+=1
  else:raise ValueError("missing path command")
  pts.append((x,y))
 if len(pts)<2:raise ValueError("empty path")
 for (a,b),(c,d) in zip(pts,pts[1:]):
  if a!=c and b!=d:raise ValueError("diagonal")
  if a==c and b==d:raise ValueError("zero-length")
 return pts
def boundary(p,r):
 x,y=p;a,b,w,h=r
 return (a-1<=x<=a+w+1 and (abs(y-b)<1 or abs(y-b-h)<1)) or (b-1<=y<=b+h+1 and (abs(x-a)<1 or abs(x-a-w)<1))
def crosses(pts,r):
 a,b,w,h=r
 for (x,y),(z,q) in zip(pts,pts[1:]):
  if x==z and a+.01<x<a+w-.01 and max(min(y,q),b)<min(max(y,q),b+h):return True
  if y==q and b+.01<y<b+h-.01 and max(min(x,z),a)<min(max(x,z),a+w):return True
 return False
def lum(s):
 c=[int(s[i:i+2],16)/255 for i in (1,3,5)]
 c=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in c]
 return sum(a*b for a,b in zip(c,(.2126,.7152,.0722)))
def audit(path,spec):
 raw=path.read_text("utf-8");h=Doc();h.feed(raw);h.close();errors=h.errors[:]
 if len(h.ids)!=len(set(h.ids)):errors.append("duplicate id")
 if h.ndetails!=1 or h.nrels!=len(spec["required_edges"]):errors.append("incomplete text alternative")
 if h.nframes!=1 or "overflow-x:auto" not in raw or "min-width:1280px" not in raw or "Desliza horizontalmente" not in raw:errors.append("broken mobile scroll")
 css="".join(h.styles)
 if re.search(r"@import|url\(\s*['\"]?\s*(https?:|//|data:|javascript:)",css,re.I):errors.append("remote CSS")
 m=re.search(r"(<svg\b.*?</svg>)",raw,re.I|re.S)
 if not m:return {"status":"FAIL","errors":errors+["no SVG"]}
 try:svg=ET.fromstring(m.group(1))
 except ET.ParseError:return {"status":"FAIL","errors":errors+["invalid XML"]}
 ns={"s":"http://www.w3.org/2000/svg"}
 if svg.get("role")!="img" or svg.get("viewBox")!="0 0 1280 720":errors.append("SVG role/viewBox mismatch")
 if svg.get("data-source-revision")!=spec["source_sha"]:errors.append("source SHA drift")
 for t in ("title","desc"):
  e=svg.findall("s:"+t,ns)
  if len(e)!=1 or not (e[0].text or "").strip():errors.append("empty accessible "+t)
 if len(svg.get("aria-labelledby","").split())!=2 or any(v not in h.ids for v in svg.get("aria-labelledby","").split()):errors.append("broken aria labels")
 nodes={};edges={}
 for g in svg.findall(".//s:g",ns):
  id=g.get("data-node")
  if not id:continue
  if id in nodes:errors.append("duplicate node")
  tr=re.fullmatch(r"translate\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)",g.get("transform",""))
  rect=g.find("s:rect",ns)
  if not tr or rect is None:errors.append("unmeasurable node");continue
  nodes[id]=(float(tr[1]),float(tr[2]),float(rect.get("width",0)),float(rect.get("height",0)))
 for e in svg.findall(".//s:path",ns):
  id=e.get("data-edge")
  if id:
   if id in edges:errors.append("duplicate connector id")
   edges[id]=e
 expected={e["id"]:e for e in spec["required_edges"]}
 if set(nodes)!=set(spec["required_nodes"]):errors.append("node set drift")
 if set(edges)!=set(expected):errors.append("edge set drift")
 for id,s in expected.items():
  e=edges.get(id)
  if e is None:continue
  a,b=s["from"],s["to"]
  if (e.get("data-from"),e.get("data-to"),e.get("data-kind"))!=(a,b,s["kind"]):errors.append("edge relation drift "+id)
  try:points=poly(e.get("d",""))
  except ValueError as ex:errors.append("geometry "+id+" "+str(ex));continue
  if a not in nodes or b not in nodes:errors.append("dangling edge "+id);continue
  if not boundary(points[0],nodes[a]) or not boundary(points[-1],nodes[b]):errors.append("detached edge "+id)
  for n,rect in nodes.items():
   if n not in (a,b) and crosses(points,rect):errors.append("edge "+id+" crosses "+n)
 for id in spec["invariant_edges"]:
  if id not in edges:errors.append("missing invariant "+id)
 tokens=dict(re.findall(r"--([a-z-]+)\s*:\s*(#[0-9a-f]{6})",css,re.I))
 if "bg" not in tokens or "muted" not in tokens or (max(lum(tokens["bg"]),lum(tokens["muted"]))+.05)/(min(lum(tokens["bg"]),lum(tokens["muted"]))+.05)<4.5:errors.append("low contrast")
 return {"status":"FAIL" if errors else "PASS","nodes":len(nodes),"edges":len(edges),"errors":errors}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--base",type=Path,default=Path(__file__).resolve().parent);args=p.parse_args()
 specs=json.loads((args.base/"graph_contract.json").read_text("utf-8"))
 result={k:audit(args.base/"outputs"/(k+".html"),v) for k,v in specs.items()}
 print(json.dumps(result,indent=2))
 sys.exit(1 if any(x["status"]!="PASS" for x in result.values()) else 0)
