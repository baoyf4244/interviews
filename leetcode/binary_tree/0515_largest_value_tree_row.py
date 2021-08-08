class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
from collections import deque

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        queue = deque([root])
        while queue:
            m = float('-inf')
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if m < node.val:
                    m = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(m)
        return res