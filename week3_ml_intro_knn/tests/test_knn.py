# tests/test_knn.py
import os, csv, unittest
from student.ml_knn import train_test_split, euclid, knn_predict, evaluate

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "points.csv")

def load_rows():
    rows = []
    with open(DATA,"r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append((float(r["x"]), float(r["y"]), r["label"]))
    return rows

class KNNTsts(unittest.TestCase):
    def test_pipeline(self):
        rows = load_rows()
        train, test = train_test_split(rows, 0.3, seed=123)
        self.assertTrue(1 <= len(test) < len(rows))
        self.assertGreater(euclid((0,0),(1,1)), 1.0)
        out = evaluate(train, test, k=3)
        self.assertGreaterEqual(out["accuracy"], 0.75)

if __name__ == "__main__":
    unittest.main()
