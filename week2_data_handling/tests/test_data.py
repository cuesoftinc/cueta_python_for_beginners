# tests/test_data.py
import os, unittest
from student.data_tasks import read_csv, coerce_types, group_sum, moving_avg, top_k

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "sales.csv")

class DataTests(unittest.TestCase):
    def test_read_and_coerce(self):
        rows = read_csv(DATA)
        self.assertTrue(len(rows) >= 6)
        rows2 = coerce_types(rows, {"units":"int","price":"float","revenue":"float"})
        self.assertIsInstance(rows2[0]["units"], int)
        self.assertIsInstance(rows2[0]["price"], float)

    def test_group_and_ma(self):
        rows = coerce_types(read_csv(DATA), {"units":"int","price":"float","revenue":"float"})
        agg = group_sum(rows, "store", "revenue")
        self.assertTrue(all(v >= 0 for v in agg.values()))
        ma = moving_avg([1,2,3,4], 3)
        self.assertEqual([round(x,2) for x in ma], [1.0, 1.5, 2.0, 3.0])

    def test_topk(self):
        out = top_k({"a":3,"b":5,"c":5,"d":1}, 3)
        self.assertEqual(out[0][0], "b")
        self.assertEqual(out[1][0], "c")
        self.assertEqual(len(out), 3)

if __name__ == "__main__":
    unittest.main()
