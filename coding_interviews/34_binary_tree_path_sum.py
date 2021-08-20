from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.results = []

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        self.dfs(root, target, [])
        return self.results

    def dfs(self, root, target, res):
        if not root:
            return
        target -= root.val
        res.append(root.val)
        if not root.left and not root.right and target == 0:
            self.results.append(res[:])

        self.dfs(root.left, target, res)
        self.dfs(root.right, target, res)
        res.pop()


node = TreeNode(5)
node.left = TreeNode(4)
node.left.left = TreeNode(11)
node.left.left.left = TreeNode(7)
node.left.left.right = TreeNode(2)
node.right = TreeNode(8)
node.right.left = TreeNode(13)
node.right.right = TreeNode(4)
node.right.right.left = TreeNode(5)
node.right.right.right = TreeNode(1)

print(Solution().pathSum(node, 22))