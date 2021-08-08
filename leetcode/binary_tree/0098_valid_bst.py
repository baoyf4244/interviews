class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.traverse(root, None, None)

    def traverse(self, root: TreeNode, mi: TreeNode, ma: TreeNode):
        if not root:
            return True

        if mi and root.val <= mi.val:
            return False

        if ma and root.val >= ma.val:
            return False

        return self.traverse(root.left, mi, root) and self.traverse(root.right, root, ma)