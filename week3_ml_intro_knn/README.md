# Week 3 — Intro to ML: k-NN Classifier (From Scratch)

Implement a simple k-nearest neighbors classifier on a tiny 2D dataset.
Learn train/test split, distance, majority vote, and accuracy/confusion matrix.

Run:
    python run_tests.py

## A worked example

A k-NN classifier labels a new point by asking which known points sit closest to it. We keep six labelled points and add one new point, `?`, at (4, 3).

```
7 | . . . . . . . .
6 | . . . . . B . .
5 | . . . . . . B .
4 | . . . . . . . .
3 | . . A . ? B . .
2 | . . . A . . . .
1 | . A . . . . . .
0 | . . . . . . . .
  +-----------------
    0 1 2 3 4 5 6 7
```

Before you read on, look at the picture and guess the label for `?`.

Step 1: measure the distance from `?` to every labelled point with `euclid`. For (5, 3) it is sqrt((5-4)² + (3-3)²) = 1.0.

Step 2: sort by distance and keep the first k = 3. These are the three nearest neighbors.

| Rank | Point  | Label | Distance to (4, 3) |
| ---- | ------ | ----- | ------------------ |
| 1    | (5, 3) | B     | 1.000              |
| 2    | (3, 2) | A     | 1.414              |
| 3    | (2, 3) | A     | 2.000              |
| 4    | (6, 5) | B     | 2.828              |
| 5    | (5, 6) | B     | 3.162              |
| 6    | (1, 1) | A     | 3.606              |

Step 3: count the labels among the top three, as `knn_predict` does.

| Label | Votes |
| ----- | ----- |
| A     | 2     |
| B     | 1     |

A wins, so the prediction for (4, 3) is `A`.

How k changes the result: with k = 1 the single nearest point is B, so the prediction is `B`; with k = 3 it is `A`; with k = 5 it is `B` again (3 votes to 2). A small k follows single points, and a larger k smooths them out, so we compare a few values of k with `evaluate`.
