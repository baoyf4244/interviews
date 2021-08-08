class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

    def dfs(self, root, total):
        if not root:
            return 0

        total = total * 10 + root.val

        if not root.left and not root.right:
            return total
        else:
            return self.dfs(root.left, total) + self.dfs(root.right, total)