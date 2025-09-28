# student/data_tasks.py — fill these in
from __future__ import annotations
from typing import List, Dict, Any, Iterable, Tuple

def read_csv(path: str) -> List[Dict[str, str]]:
    """Return list of dict rows from a simple CSV. Strip header/field spaces.""" 
    raise NotImplementedError

def coerce_types(rows: List[Dict[str,str]], schema: Dict[str,str]) -> List[Dict[str,Any]]:
    """Cast columns to given types: 'int','float','str'. Unlisted columns stay str.""" 
    raise NotImplementedError

def group_sum(rows: List[Dict[str,Any]], key: str, value: str) -> Dict[str,float]:
    """Sum 'value' by 'key'. Missing/invalid values treated as 0.0.""" 
    raise NotImplementedError

def moving_avg(xs: List[float], k: int) -> List[float]:
    """Right-aligned window average of size k. For i<k-1, average xs[:i+1].""" 
    raise NotImplementedError

def top_k(items: Dict[str,float], k: int) -> List[Tuple[str,float]]:
    """Return top-k (key,val) pairs sorted by val desc, then key asc.""" 
    raise NotImplementedError
