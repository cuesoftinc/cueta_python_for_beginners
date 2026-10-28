# Solutions — Explanation & Edge Cases

- `greet`: `.strip()` trims; `.title()` handles multi-word names (e.g., "ada lovelace").
- `reverse_words`: `.split()` collapses multiple spaces — handy for noisy input.
- `factorial`: iterative, avoids recursion limits; validates `n >= 0`.
- `max_diff`: empty iterable → `None` (tests check this).
- `word_count`: regex `[a-z']+` keeps contractions as single tokens.
