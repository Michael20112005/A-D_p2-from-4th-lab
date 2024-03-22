import unittest

def binary_search(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def find_three_numbers(arr, P):
    arr.sort()
    n = len(arr)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == P:
                return True
            elif current_sum < P:
                if binary_search(arr, left, right, P - arr[i] - arr[left]):
                    return True
                left += 1
            else:
                right -= 1
    return False

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
