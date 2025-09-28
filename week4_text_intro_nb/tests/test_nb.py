# tests/test_nb.py
import os, csv, unittest
from student.nb_sentiment import tokenize, train_nb, predict_one, evaluate

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "sentiment.csv")

def load_rows():
    rows = []
    with open(DATA,"r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append((r["text"], r["label"]))
    return rows

class NBTsts(unittest.TestCase):
    def test_train_and_eval(self):
        rows = load_rows()
        model = train_nb(rows[:8], alpha=1.0)
        acc = evaluate(model, rows[8:])
        self.assertGreaterEqual(acc, 0.6)  # tiny set, modest bar
        self.assertIn(predict_one(model, "great quality and amazing"), {"pos","neg"})

if __name__ == "__main__":
    unittest.main()
