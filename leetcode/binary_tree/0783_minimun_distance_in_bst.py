class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.prev = float('-inf')
        self.ans = float('inf')

    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.dfs(root)
        return self.ans

    def dfs(self, root: TreeNode):
        if not root:
            return
        self.dfs(root.left)
        self.ans = min(self.ans, self.prev - root.val)
        self.prev = root.val
        self.dfs(root.right)
