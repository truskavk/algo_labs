import unittest

from src.boyer_moore import boyer_moore

class TestBoyerMoore(unittest.TestCase):
    def test_substring_found(self):
        s = "abcaabcabcaabc"
        substring = "aabc"
        expected = [3, 10]
        self.assertEqual(boyer_moore(s, substring), expected)

    def test_substring_not_found(self):
        s = "Hello, world!"
        substring = "Python"
        expected = []
        self.assertEqual(boyer_moore(s, substring), expected)

    def test_empty_string(self):
        s = ""
        substring = "Python"
        expected = []
        self.assertEqual(boyer_moore(s, substring), expected)

    def test_substring_at_start(self):
        s = "Hello, world!"
        substring = "Hello"
        expected = [0]
        self.assertEqual(boyer_moore(s, substring), expected)

    def test_substring_at_end(self):
        s = "Hello, world!"
        substring = "world!"
        expected = [7]
        self.assertEqual(boyer_moore(s, substring), expected)

    def test_case_sensitive_search(self):
        s = "Hello, world!"
        substring = "hello"
        expected = []
        self.assertEqual(boyer_moore(s, substring), expected)

if __name__ == '__main__':
    unittest.main()