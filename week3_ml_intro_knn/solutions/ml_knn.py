# solutions/ml_knn.py
from __future__ import annotations
from typing import List, Tuple, Dict
import math, random

Row = Tuple[float,float,str]

def train_test_split(rows: List[Row], test_ratio: float=0.3, seed: int=0):
    rnd = random.Random(seed)
    rows2 = rows[:]
    rnd.shuffle(rows2)
    n_test = max(1, int(len(rows2)*test_ratio))
    return rows2[n_test:], rows2[:n_test]

def euclid(a: Tuple[float,float], b: Tuple[float,float]) -> float:
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def knn_predict(train: List[Row], point: Tuple[float,float], k: int=3) -> str:
    dists = [ (euclid((x,y), point), lab) for (x,y,lab) in train ]
    dists.sort(key=lambda t: t[0])
    k = max(1, min(k, len(dists)))
    top = dists[:k]
    votes: Dict[str,int] = {}
    for _, lab in top:
        votes[lab] = votes.get(lab,0)+1
    best = sorted(votes.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
    return best

def evaluate(train: List[Row], test: List[Row], k: int=3) -> Dict[str,object]:
    cm: Dict[Tuple[str,str],int] = {}
    correct = 0
    for x,y,lab in test:
        pred = knn_predict(train, (x,y), k)
        if pred == lab: correct += 1
        cm[(lab,pred)] = cm.get((lab,pred),0)+1
    acc = correct / max(1,len(test))
    return {"accuracy": acc, "cm": cm}
