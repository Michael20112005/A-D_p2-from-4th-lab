import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from find_union import weddings_and_tribes


class TestWeddingsAndTribes(unittest.TestCase):

    def test_good_case(self):
        pairs_list = [(1, 2), (2, 3), (3, 4), (5, 6)]
        total_pairs, possible_pairs = weddings_and_tribes(pairs_list)
        self.assertEqual(total_pairs, 4)
        self.assertSetEqual(possible_pairs, {(1, 6), (5, 2), (5, 4), (3, 6)})

    def test_bad_case(self):
        pairs_list = [(1, 2), (2, 3), (3, 4), (5, 6), (1, 5)]
        total_pairs, possible_pairs = weddings_and_tribes(pairs_list)
        self.assertEqual(total_pairs, 0)
        self.assertSetEqual(possible_pairs, set())

    def test_another_good_case(self):
        pairs_list = [(1, 2), (2, 3), (1, 3), (4, 5)]
        total_pairs, possible_pairs = weddings_and_tribes(pairs_list)
        self.assertEqual(total_pairs, 3)
        self.assertSetEqual(possible_pairs, {(3, 4), (1, 4), (5, 2)})


if __name__ == '__main__':
    unittest.main()
    
