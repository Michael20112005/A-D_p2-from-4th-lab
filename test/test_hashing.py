import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from hashing import find_3_numbers_sum


class TestFindThreeNumbers(unittest.TestCase):

    def test_find_numbers_with_sum_good_case(self):
        array = [1, 2, 3, 6]
        p = 6
        self.assertTrue(find_3_numbers_sum(array, p))

    def test_find_three_numbers_LoL_case(self):
        array = [2, 100, 60, 1]
        p = 41
        self.assertFalse(find_3_numbers_sum(array, p))

    def test_find_three_numbers_nonexistent_case(self):
        array = [2, 3]
        p = 7
        self.assertFalse(find_3_numbers_sum(array, p))


if __name__ == '__main__':
    unittest.main()
