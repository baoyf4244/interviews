class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        res = self.dp(root)
        return max(res)

    def dp(self, root):
        if not root:
            return [0, 0]

        left = self.dp(root.left)
        right = self.dp(root.right)

        rob_root = root.val + left[1] + right[1]
        not_rob_root = max(left) + max(right)
        return [rob_root, not_rob_root]