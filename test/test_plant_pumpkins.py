import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from plant_pumpkins import plant_pumpkins_route


class TestPlantPumpkinsRoute(unittest.TestCase):

    def test_matrix_3x3(self):
        matrix = [
            [1, 2, 3],
            [8, 7, 6],
            [9, 10, 11]
        ]
        expected_result = [1, 2, 3, 6, 7, 8, 9, 10, 11]
        self.assertEqual(plant_pumpkins_route(matrix), expected_result)

    def test_matrix_2x4(self):
        matrix = [
            [1, 2, 3, 4],
            [8, 7, 6, 5]
        ]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(plant_pumpkins_route(matrix), expected_result)

    def test_matrix_4x2(self):
        matrix = [
            [1, 2],
            [6, 5],
            [7, 8],
            [12, 11]
        ]
        expected_result = [1, 2, 5, 6, 7, 8, 11, 12]
        self.assertEqual(plant_pumpkins_route(matrix), expected_result)


if __name__ == '__main__':
    unittest.main()
