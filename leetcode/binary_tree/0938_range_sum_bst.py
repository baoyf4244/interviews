class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.dfs(root, low, high)
        return self.ans

    def dfs(self, root, low, high):
        if root:
            if low <= root.val <= high:
                self.ans += root.val
            if root.val > low:
                self.dfs(root.left, low, high)
            if root.val < high:
                self.dfs(root.right, low, high)
