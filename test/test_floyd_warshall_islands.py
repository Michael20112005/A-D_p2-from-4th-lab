import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import numpy as np
from floyd_warshall_islands import calculate_total_cable_length


class TestCableLength(unittest.TestCase):

    def test_small_graph(self):
        adj_matrix = np.array([
            [0, 1, np.inf],
            [1, 0, 1],
            [np.inf, 1, 0]
        ])
        result = calculate_total_cable_length(adj_matrix)
        expected = 8.0
        self.assertAlmostEqual(result, expected, places=2)

    def test_medium_graph(self):
        adj_matrix = np.array([
            [0, 2, np.inf, 6],
            [2, 0, 3, 8],
            [np.inf, 3, 0, np.inf],
            [6, 8, np.inf, 0]
        ])
        result = calculate_total_cable_length(adj_matrix)
        expected = 70.0
        self.assertAlmostEqual(result, expected, places=2)

    def test_large_graph(self):
        adj_matrix = np.array([
            [0, 2, np.inf, 6, np.inf],
            [2, 0, 3, 8, 5],
            [np.inf, 3, 0, np.inf, 7],
            [6, 8, np.inf, 0, 9],
            [np.inf, 5, 7, 9, 0]
        ])
        result = calculate_total_cable_length(adj_matrix)
        expected = 126.0
        self.assertAlmostEqual(result, expected, places=2)


if __name__ == '__main__':
    unittest.main()
