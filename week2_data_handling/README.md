# Week 2 — Data Handling (CSV → Insights)

You’ll write stdlib-only ETL utilities: read CSV, coerce types, aggregate, smooth, and rank.

## Implement in `student/data_tasks.py`
- `read_csv(path)` → list[dict]
- `coerce_types(rows, schema)` → cast columns to int/float/str
- `group_sum(rows, key, value)` → dict of sums
- `moving_avg(xs, k)` → right-aligned window
- `top_k(items, k)` → top k by value

Run:
    python run_tests.py
