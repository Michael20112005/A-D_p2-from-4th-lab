import math
from calculate_max_length import calculate_max_length
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


class TestCalculateMaxLength(unittest.TestCase):

    def test_good_input(self):
        w = 4
        heights = [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91, 25, 17, 88, 66, 28, 2, 95, 97,
                   60, 93, 40, 70, 75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39, 72]
        result = calculate_max_length(w, heights)
        self.assertEqual(result, 2738.18)

    def test_single_pole(self):
        w = 5
        heights = [50]
        result = calculate_max_length(w, heights)
        self.assertEqual(result, 0.0)

    def test_max_heights(self):
        w = 1
        heights = [100, 100, 100, 100, 100]
        result = calculate_max_length(w, heights)
        self.assertAlmostEqual(result, 4 * math.sqrt(1 + 99 ** 2), places=2)

    def test_large_w(self):
        w = 100
        heights = [1, 1, 1, 1, 1]
        result = calculate_max_length(w, heights)
        self.assertAlmostEqual(result, 4 * math.sqrt(100 ** 2 + 0 ** 2), places=2)


if __name__ == '__main__':
    unittest.main()
