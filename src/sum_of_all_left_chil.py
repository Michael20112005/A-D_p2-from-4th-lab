class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    if root is None:
        return 0

    if root.left is not None and root.left.left is None and root.left.right is None:
        return root.left.value + branchSums(root.right)
    else:
        return branchSums(root.left) + branchSums(root.right)


root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.right.left = BinaryTree(15)
root.right.right = BinaryTree(7)

print(branchSums(root))