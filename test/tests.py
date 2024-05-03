import unittest
import numpy as np
import csv

class TestSubmarineCableLength(unittest.TestCase):

    def read_adj_matrix_from_file(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            adj_matrix = np.array([[int(val) for val in row] for row in reader])
        return adj_matrix


    def test_valid_distances(self):
        adj_matrix = self.read_adj_matrix_from_file('islands.csv')

        self.assertTrue(total_cable_length >= 0)


    def test_negative_distances(self):
        adj_matrix = self.read_adj_matrix_from_file('islands.csv')

        self.assertTrue(total_cable_length < 0)


    def test_large_distances(self):
        adj_matrix = self.read_adj_matrix_from_file('islands.csv')

        self.assertTrue(total_cable_length < 999999)


if __name__ == '__main__':
    unittest.main()