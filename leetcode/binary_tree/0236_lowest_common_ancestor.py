class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return self.ans

        self.dfs(root, p, q)
        return self.ans

    def dfs(self, root: TreeNode, q: TreeNode, p: TreeNode):
        if not root:
            return False
        l_son = self.dfs(root.left, p, q)
        r_son = self.dfs(root.right, p, q)

        if (l_son and r_son) or ((root.val == p.val or root.val == q.val) and (l_son or r_son)):
            self.ans = root

        return l_son or r_son or (root.val == p.val or root.val == q.val)
