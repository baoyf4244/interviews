from typing import List
from collections import deque

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
        level = deque([root])
        left_first = True
        while level:
            res = []
            for i in range(len(level)):
                node = level.popleft()
                res.append(node.val)

                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            if left_first:
                results.append(res)
            else:
                results.append(res[::-1])
            left_first = not left_first

        return results
