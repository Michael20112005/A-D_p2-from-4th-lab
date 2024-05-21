import unittest
import os
import sys
from hashing import find_3_numbers_sum
test_file_path = os.path.abspath(__file__)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)


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
