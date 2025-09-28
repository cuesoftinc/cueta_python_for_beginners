# student/nb_sentiment.py
from __future__ import annotations
from typing import List, Tuple, Dict
import re, math

Row = Tuple[str, str]  # (text, label)

def tokenize(s: str) -> List[str]:
    """Lowercase a-z tokens.""" 
    raise NotImplementedError

def train_nb(rows: List[Row], alpha: float=1.0) -> Dict[str,object]:
    """Return model with priors and per-class word counts (Laplace smoothing).""" 
    raise NotImplementedError

def predict_one(model: Dict[str,object], text: str) -> str:
    """Return 'pos' or 'neg' using log-probabilities.""" 
    raise NotImplementedError

def evaluate(model: Dict[str,object], rows: List[Row]) -> float:
    """Return accuracy over rows.""" 
    raise NotImplementedError
