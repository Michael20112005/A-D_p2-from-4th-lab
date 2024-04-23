import unittest

class TestRabinKarpSearch(unittest.TestCase):
    def test_basic_match(self):
        haystack = "hello world"
        needle = "world"
        expected = [6]
        self.assertEqual(rabin_karp_search(haystack, needle), expected)

    def test_multiple_matches(self):
        haystack = "abracadabra"
        needle = "abra"
        expected = [0, 7]
        self.assertEqual(rabin_karp_search(haystack, needle), expected)

    def test_no_match(self):
        haystack = "the quick brown fox"
        needle = "jumps"
        expected = []
        self.assertEqual(rabin_karp_search(haystack, needle), expected)

    def test_empty_strings(self):
        haystack = ""
        needle = "nonempty"
        expected = []
        self.assertEqual(rabin_karp_search(haystack, needle), expected)

        haystack = "nonempty"
        needle = ""
        self.assertEqual(rabin_karp_search(haystack, needle), expected)

        haystack = ""
        needle = ""
        self.assertEqual(rabin_karp_search(haystack, needle), expected)

if __name__ == '__main__':
    unittest.main()