class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        s = self.dfs(root)
        if s == 0:
            return None
        return root

    def dfs(self, root):
        if not root:
            return 0

        sum = 0
        left = sum + self.dfs(root.left)
        if left == 0:
            root.left = None

        right = sum + self.dfs(root.right)

        if right == 0:
            root.right = None

        return left + right + root.val
