# solutions/data_tasks.py — reference answers
from __future__ import annotations
from typing import List, Dict, Any, Iterable, Tuple

def read_csv(path: str) -> List[Dict[str, str]]:
    rows: List[Dict[str,str]] = []
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    if not lines: return rows
    headers = [h.strip() for h in lines[0].split(",")]
    for ln in lines[1:]:
        if not ln.strip(): continue
        fields = [x.strip() for x in ln.split(",")]
        if len(fields) != len(headers): continue
        rows.append({h: fields[i] for i, h in enumerate(headers)})
    return rows

def coerce_types(rows: List[Dict[str,str]], schema: Dict[str,str]) -> List[Dict[str,Any]]:
    out: List[Dict[str,Any]] = []
    for r in rows:
        rr: Dict[str,Any] = {}
        for k, v in r.items():
            t = schema.get(k, "str")
            if t == "int":
                try: rr[k] = int(v)
                except: rr[k] = 0
            elif t == "float":
                try: rr[k] = float(v)
                except: rr[k] = 0.0
            else:
                rr[k] = v
        out.append(rr)
    return out

def group_sum(rows: List[Dict[str,Any]], key: str, value: str) -> Dict[str,float]:
    agg: Dict[str,float] = {}
    for r in rows:
        k = str(r.get(key, ""))
        try: v = float(r.get(value, 0.0))
        except: v = 0.0
        agg[k] = agg.get(k, 0.0) + v
    return agg

def moving_avg(xs: List[float], k: int) -> List[float]:
    if k < 1: raise ValueError("k>=1")
    out: List[float] = []
    total = 0.0
    for i, val in enumerate(xs):
        total += val
        if i >= k: total -= xs[i-k]
        win = min(i+1, k)
        out.append(total / win)
    return out

def top_k(items: Dict[str,float], k: int) -> List[Tuple[str,float]]:
    pairs = sorted(items.items(), key=lambda kv: (-kv[1], kv[0]))
    return pairs[:k]
