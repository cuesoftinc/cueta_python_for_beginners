# solutions/nb_sentiment.py
from __future__ import annotations
from typing import List, Tuple, Dict
import re, math

Row = Tuple[str, str]
WORD = re.compile(r"[a-z']+")

def tokenize(s: str) -> List[str]:
    return [t.strip("'") for t in WORD.findall(s.lower()) if t]

def train_nb(rows: List[Row], alpha: float=1.0) -> Dict[str,object]:
    classes = {"pos":0, "neg":0}
    vocab = set()
    counts = {"pos":{}, "neg":{}}
    for text, lab in rows:
        classes[lab] += 1
        toks = tokenize(text)
        for t in toks:
            vocab.add(t)
            d = counts[lab]; d[t] = d.get(t,0)+1
    total = sum(classes.values())
    priors = {c: classes[c]/total for c in classes}
    totals = {c: sum(counts[c].values()) for c in classes}
    return {"priors":priors, "counts":counts, "totals":totals, "alpha":alpha, "vocab":vocab}

def predict_one(model: Dict[str,object], text: str) -> str:
    toks = tokenize(text)
    alpha = model["alpha"]; vocab = model["vocab"]
    best_c, best = None, -1e99
    for c in ("pos","neg"):
        logp = math.log(model["priors"][c] + 1e-12)
        total = model["totals"][c]; counts = model["counts"][c]
        denom = total + alpha * (len(vocab) or 1)
        for t in toks:
            num = counts.get(t,0) + alpha
            logp += math.log(num/denom)
        if logp > best: best, best_c = logp, c
    return best_c or "neg"

def evaluate(model: Dict[str,object], rows: List[Row]) -> float:
    correct = 0
    for text, lab in rows:
        if predict_one(model, text) == lab: correct += 1
    return correct / max(1,len(rows))
