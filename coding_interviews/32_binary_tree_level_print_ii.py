from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        results = []
        level = [root]
        res = []
        while level:
            for i in range(len(level)):
                node = level.pop(0)
                res.append(node.val)

                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)
            results.append(res)
            res = []

        return results
