import unittest

from src.has_cycle import has_cycle

class TestCycleDetection(unittest.TestCase):
    def test_no_cycle(self):
        g = {
            0: [1],
            1: [2],
            2: [3]
        }

        self.assertFalse(has_cycle(g))

    def test_single_node(self):
        g = {}
        self.assertFalse(has_cycle(g))

    def test_cycle(self):
        g = {
            0: [1],
            1: [2],
            2: [0]
        }

        self.assertTrue(has_cycle(g))

    def test_disconnected_graph(self):
        g = {
            0: [1],
            2: [3]
        }

        self.assertFalse(has_cycle(g))

    def test_self_loop(self):
        g = {
            0: [0]
        }

        self.assertTrue(has_cycle(g))

if __name__ == '__main__':
    unittest.main()