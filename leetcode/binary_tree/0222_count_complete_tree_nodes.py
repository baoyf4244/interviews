class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def compute_depth(self, root):
        d = 0
        node = root
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, root, d, idx):
        left, right = 0, 2**d - 1
        node = root
        for i in range(d):
            mid = left + (right - left) // 2
            if idx <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
        return node is not None

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        d = self.compute_depth(root)
        if d == 0:
            return 1

        left, right = 0, 2**d - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.exists(root, d, mid):
                left = mid + 1
            else:
                right = mid - 1

        return 2**d - 1 + left


