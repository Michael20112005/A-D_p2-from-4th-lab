import unittest
import numpy as np
import csv

from src.floyd_warshall_islands import main


class TestSubmarineCableLength(unittest.TestCase):

    def read_adj_matrix_from_file(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            adj_matrix = np.array([[int(val) for val in row] for row in reader])
        return adj_matrix

    def setUp(self):
        self.total_cable_length = main()

    def test_valid_distances(self):
        adj_matrix = self.read_adj_matrix_from_file('../src/Islands.csv')
        self.assertTrue(self.total_cable_length >= 0)

    def test_cable_length_within_range(self):
        adj_matrix = self.read_adj_matrix_from_file('../src/Islands.csv')
        self.assertTrue(0 <= self.total_cable_length < 999999)

    def test_large_distances(self):
        adj_matrix = self.read_adj_matrix_from_file('../src/Islands.csv')
        self.assertTrue(self.total_cable_length < 999999)


        #too general tests. Do not cover extreme cases


if __name__ == '__main__':
    unittest.main()
