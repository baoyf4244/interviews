# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from collections import deque

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = -1
        if not root:
            return 0

        queue = deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.children:
                    queue.extend(node.children)

            depth += 1
        return depth