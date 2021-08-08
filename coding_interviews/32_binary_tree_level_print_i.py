from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        results = []
        level = [root]
        while level:
            for i in range(len(level)):
                node = level.pop(0)
                results.append(node.val)

                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)

        return results
