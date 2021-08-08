class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            if root.left and root.right:
                mi = self.get_min(root.right)
                root.val = mi.val
                root.right = self.deleteNode(root.right, mi.val)
        return root

    def get_min(self, root):
        mi = root
        while mi.left:
            mi = mi.left
        return mi