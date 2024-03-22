import unittest

class TestBranchSums(unittest.TestCase):
    def test_branch_sums_empty_tree(self):
        self.assertEqual(branchSums(None), 0)

    def test_branch_sums_single_node(self):
        root = BinaryTree(3)
        self.assertEqual(branchSums(root), 3)

    def test_branch_sums_complex_tree(self):
        root = BinaryTree(5)
        root.left = BinaryTree(2)
        root.right = BinaryTree(7)
        root.left.left = BinaryTree(1)
        root.left.right = BinaryTree(3)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(8)

        self.assertEqual(branchSums(root), 56)

if __name__ == '__main__':
    unittest.main()