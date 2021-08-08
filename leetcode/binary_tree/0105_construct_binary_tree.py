from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, preorder, pre_low, pre_high, inorder, in_low, in_high):
        if pre_low > pre_high or in_low > in_high:
            return None

        root = TreeNode(preorder[pre_low])

        index = in_low
        for i in range(in_low + 1, in_high + 1):
            if inorder[i] == preorder[pre_low]:
                index = i
                break

        root.left = self.build(preorder, pre_low + 1, pre_low + (index - in_low), inorder, in_low, index -1)
        root.right = self.build(preorder, pre_low + (index - in_low) + 1, pre_high, inorder, index + 1, in_high)
        return root