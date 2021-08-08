class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A:
            return False

        if not B:
            return False

        if self.is_equal(A, B):
            return True

        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def is_equal(self, a, b):
        if not b:
            return True

        if not a:
            return False

        if a.val == b.val:
            return self.is_equal(a.left, b.left) and self.is_equal(a.right, b.right)