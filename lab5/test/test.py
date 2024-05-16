import unittest
from src.max_experience import max_experience

class TestMaxExperienceFunction(unittest.TestCase):
    def test_case1(self):
        experience = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1],
        ]
        expected = 12

        self.assertEqual(max_experience(experience), expected)

    def test_case2(self):
        experience = [
            [9999]
        ]
        expected = 9999

        self.assertEqual(max_experience(experience), expected)

    def test_case3(self):
        experience = [
            [0],
            [1, 1],
            [0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 1, 0]
        ]
        expected = 3
        
        self.assertEqual(max_experience(experience), expected)

if __name__ == '__main__':
    unittest.main()