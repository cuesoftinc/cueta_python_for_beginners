# solutions/homework.py — instructor solution
from __future__ import annotations
from typing import List, Dict, Any, Iterable, Optional
import re

def add(a: float, b: float) -> float:
    return a + b

def is_even(n: int) -> bool:
    return (n % 2) == 0

def greet(name: str) -> str:
    name = name.strip().title()
    return f"Hello, {name}!"

def count_vowels(s: str) -> int:
    return sum(1 for ch in s.lower() if ch in 'aeiou')

def reverse_words(sentence: str) -> str:
    parts = sentence.split()
    parts.reverse()
    return " ".join(parts)

def fizzbuzz(n: int) -> List[str]:
    out = []
    for i in range(1, n+1):
        if i % 15 == 0: out.append("FizzBuzz")
        elif i % 3 == 0: out.append("Fizz")
        elif i % 5 == 0: out.append("Buzz")
        else: out.append(str(i))
    return out

def factorial(n: int) -> int:
    if n < 0: raise ValueError("n must be >= 0")
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

def unique_sorted(nums: Iterable[float]) -> List[float]:
    return sorted(set(nums))

def max_diff(nums: Iterable[float]) -> Optional[float]:
    nums = list(nums)
    if not nums: return None
    return max(nums) - min(nums)

def word_count(filepath: str) -> Dict[str, int]:
    txt = open(filepath, "r", encoding="utf-8").read().lower()
    words = re.findall(r"[a-z']+", txt)
    counts: Dict[str,int] = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts
