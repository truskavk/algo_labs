import unittest

from find_sum import find_sum

class FindSumTest(unittest.TestCase):
    def testcase1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertEqual(find_sum(nums, target), expected)

    def testcase2(self):
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        self.assertEqual(find_sum(nums, target), expected)

    def testcase3(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        self.assertEqual(find_sum(nums, target), expected)

    def testcase4(self):
        nums = [3, 5]
        target = 6
        expected = -1
        self.assertEqual(find_sum(nums, target), expected)

if __name__ == '__main__':
    unittest.main()