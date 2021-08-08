class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return float('-inf')
        total = float('-inf')
        self.dfs(root, total)
        return total

    def dfs(self, root, total):
        if not root:
            return

        