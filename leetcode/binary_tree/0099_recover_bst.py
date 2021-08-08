class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        if root.left:
            self.recoverTree(root.left)
            if root.left.val > root.val:
                root.left.val, root.val = root.val, root.left.val

        if root.right:
            self.recoverTree(root.right)
            if root.right.val < root.val:
                root.right.val, root.val = root.val, root.right.val