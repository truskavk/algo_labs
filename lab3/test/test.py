import unittest

from src.postorder import post_order_traversal, BinaryTree

class TestPostorderTraversal(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(1)
        self.root.left = BinaryTree(2)
        self.root.right = BinaryTree(3)
        self.root.left.left = BinaryTree(4)
        self.root.left.right = BinaryTree(5)
        self.root.right.left = BinaryTree(6)
        self.root.right.right = BinaryTree(7)

    def test_postorder_iterative(self):
        result = post_order_traversal(self.root)
        self.assertEqual(result, [4, 5, 2, 6, 7, 3, 1])

    def test_empty_tree(self):
        empty_tree = None
        result = post_order_traversal(empty_tree)
        self.assertEqual(result, [])

    def test_single_node(self):
        single_node_tree = BinaryTree(42)
        result = post_order_traversal(single_node_tree)
        self.assertEqual(result, [42])

    def test_tree_with_one_child(self):
        tree_with_one_child = BinaryTree(1)
        tree_with_one_child.left = BinaryTree(2)
        result = post_order_traversal(tree_with_one_child)
        self.assertEqual(result, [2, 1])

    def test_tree_with_two_children(self):
        tree_with_two_children = BinaryTree(1)
        tree_with_two_children.left = BinaryTree(2)
        tree_with_two_children.right = BinaryTree(3)
        result = post_order_traversal(tree_with_two_children)
        self.assertEqual(result, [2, 3, 1])
