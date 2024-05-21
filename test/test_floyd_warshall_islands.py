import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from floyd_warshall_islands import calculate_total_cable_length

class TestSubmarineCableLength(unittest.TestCase):

    def setUp(self):
        self.INF = float('inf')

    def test_valid_distances(self):
        adj_matrix = np.array([
            [0, 1, self.INF],
            [1, 0, 1],
            [self.INF, 1, 0]
        ])
        total_cable_length = calculate_total_cable_length(adj_matrix)
        self.assertAlmostEqual(total_cable_length, 5)  # Expected total length

    def test_cable_length_within_range(self):
        adj_matrix = np.array([
            [0, 2, self.INF, 1],
            [2, 0, 3, self.INF],
            [self.INF, 3, 0, 1],
            [1, self.INF, 1, 0]
        ])
        total_cable_length = calculate_total_cable_length(adj_matrix)
        self.assertAlmostEqual(total_cable_length, 11)  # Expected total length

    def test_large_distances(self):
        adj_matrix = np.array([
            [0, 1, self.INF],
            [1, 0, 1000000],
            [self.INF, 1000000, 0]
        ])
        total_cable_length = calculate_total_cable_length(adj_matrix)
        self.assertAlmostEqual(total_cable_length, 1000002)  # Expected total length

if __name__ == '__main__':
    unittest.main()
