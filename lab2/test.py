import unittest

from merge_time import merge_time

class TestMergeTimeRanges(unittest.TestCase):
    def test_merge_time_ranges(self):
        input_ranges = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        self.assertEqual(merge_time(input_ranges), [(0, 1), (3, 8), (9, 12)])

    def test_empty_input(self):
        input_ranges = []
        self.assertEqual(merge_time(input_ranges), [])

    def test_no_overlap(self):
        input_ranges = [(0, 1), (3, 5), (6, 8), (10, 12)]
        self.assertEqual(merge_time(input_ranges), input_ranges)

    def test_single_range(self):
        input_ranges = [(0, 1)]
        self.assertEqual(merge_time(input_ranges), input_ranges)

    def test_all_overlap(self):
        input_ranges = [(0, 5), (3, 8), (2, 6)]
        self.assertEqual(merge_time(input_ranges), [(0, 8)])

if __name__ == '__main__':
    unittest.main()