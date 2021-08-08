class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.tilt = 0

    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.traverse(root)
        return self.tilt

    def traverse(self, root):
        if not root:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.tilt += abs(left - right)
        return root.val + left + right
