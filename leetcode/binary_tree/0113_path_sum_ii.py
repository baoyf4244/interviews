from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        paths = []
        path = []
        self.dfs(root, sum, path, paths)
        return paths

    def dfs(self, root, total, path, paths):
        if not root:
            return
        total -= root.val
        path.append(root.val)
        if not root.left and not root.right and total == 0:
            paths.append(path[:])
        self.dfs(root.left, total, path, paths)
        self.dfs(root.right, total, path, paths)
        path.pop()
