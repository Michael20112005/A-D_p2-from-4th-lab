import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from sum_of_all_left_child import branchSums, BinaryTree


class TestBranchSums(unittest.TestCase):

    def test_good_case(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)

        self.assertEqual(branchSums(root), 24)

    def test_bad_case(self):
        root = None

        self.assertEqual(branchSums(root), 0)

    def test_empty(self):
        root = BinaryTree(0)  # Creating a tree with only the root node

        self.assertEqual(branchSums(root), 0)  # Expected sum of values is 0


if __name__ == '__main__':
    unittest.main()
