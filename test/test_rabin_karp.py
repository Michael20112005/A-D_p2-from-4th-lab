from rabin_karp import rabin_karp_search
import unittest


class TestRabinKarpSearch(unittest.TestCase):

    def test_good_case(self):
        haystack = "ABABDABACDABABCABAB"
        needle = "AB"
        expected = [0, 2, 5, 10, 12, 15, 17]
        self.assertEqual(rabin_karp_search(haystack, needle), expected)

    def test_bad_case(self):
        haystack = "ABCDEF"
        needle = "XYZ"
        self.assertEqual(rabin_karp_search(haystack, needle), [])

    def test_empty(self):
        haystack = "ABCDEF"
        needle = ""
        self.assertEqual(rabin_karp_search(haystack, needle), [])


if __name__ == '__main__':
    unittest.main()
