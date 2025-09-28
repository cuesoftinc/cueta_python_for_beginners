# tests/test_core.py
import os, unittest
from student.homework import (
    add, is_even, greet, count_vowels, reverse_words, fizzbuzz,
    factorial, unique_sorted, max_diff, word_count
)

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "little_text.txt")

class BasicsTests(unittest.TestCase):
    def test_add_and_even(self):
        self.assertAlmostEqual(add(2,3), 5)
        self.assertTrue(is_even(4)); self.assertFalse(is_even(5))

    def test_greet_and_vowels(self):
        self.assertEqual(greet("  ada  "), "Hello, Ada!")
        self.assertEqual(count_vowels("AEioux"), 5)

    def test_reverse_and_fizzbuzz(self):
        self.assertEqual(reverse_words("One   two  three"), "three two One")
        self.assertEqual(fizzbuzz(5), ["1","2","Fizz","4","Buzz"])

    def test_factorial_and_unique(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError): factorial(-1)
        self.assertEqual(unique_sorted([3,1,2,3,2]), [1,2,3])

    def test_maxdiff_and_wc(self):
        self.assertEqual(max_diff([1,5,3]), 4)
        self.assertIsNone(max_diff([]))
        wc = word_count(DATA)
        self.assertTrue(isinstance(wc, dict) and wc.get("the",0)>=1)

if __name__ == "__main__":
    unittest.main()
