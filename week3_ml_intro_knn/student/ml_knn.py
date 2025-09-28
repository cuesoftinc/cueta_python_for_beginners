# student/ml_knn.py
from __future__ import annotations
from typing import List, Tuple, Dict
import math, random

Row = Tuple[float,float,str]  # (x, y, label)

def train_test_split(rows: List[Row], test_ratio: float=0.3, seed: int=0):
    """Return (train, test) random split.""" 
    raise NotImplementedError

def euclid(a: Tuple[float,float], b: Tuple[float,float]) -> float:
    """Euclidean distance between 2D points.""" 
    raise NotImplementedError

def knn_predict(train: List[Row], point: Tuple[float,float], k: int=3) -> str:
    """Return predicted label by majority vote among k nearest neighbors.""" 
    raise NotImplementedError

def evaluate(train: List[Row], test: List[Row], k: int=3) -> Dict[str,object]:
    """Return {'accuracy': float, 'cm': {(true,pred):count}}.""" 
    raise NotImplementedError
