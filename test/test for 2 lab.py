import unittest

class TestFindThreeNumbers(unittest.TestCase):

    def test_example(self):
        arr = [1, 2, 3]
        P = 6
        self.assertTrue(find_three_numbers(arr, P))

    def test_no_solution(self):
        arr = [1, 2, 3]
        P = 7
        self.assertFalse(find_three_numbers(arr, P))

    def test_large_input(self):
        arr = [100001, 200002, 300003]
        P = 600006
        self.assertTrue(find_three_numbers(arr, P))


if __name__ == '__main__':
    unittest.main()