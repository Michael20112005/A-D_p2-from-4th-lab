from main import calculate_max_length
import unittest

class TestCalculateMaxLength(unittest.TestCase):

    def test_good_input(self):
        w = 7
        heights = [69, 85, 31, 78, 91, 68, 20, 69, 74, 41, 57, 89, 35, 40, 53, 47, 77, 13, 93, 83, 69, 62, 37, 92, 16,
                   95, 85, 38, 2, 69, 86, 81, 66, 2, 29, 1, 94, 7, 69, 69, 30, 87, 63, 50, 69, 88, 10, 54, 93]
        result = calculate_max_length(w, heights)
        self.assertEqual(result, 1804.31)

    def test_bad_input(self):
        w = -1  # Невірна відстань
        heights = [69, 85, 31, 78]
        result = calculate_max_length(w, heights)
        self.assertEqual(result, 0.0)

    def test_empty_input(self):
        w = 7
        heights = []
        result = calculate_max_length(w, heights)
        self.assertEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()
