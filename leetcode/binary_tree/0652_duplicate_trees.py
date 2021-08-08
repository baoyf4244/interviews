from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sub_trees = {}
        self.results = []

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return None

        self.traverse(root)
        return self.results

    def traverse(self, root):
        if not root:
            return '#'

        left = self.traverse(root.left)
        right = self.traverse(root.right)

        sub_tree = '{} {} {}'.format(left, right, root.val)
        if sub_tree not in self.sub_trees:
            self.sub_trees[sub_tree] = 1
        else:
            if self.sub_trees[sub_tree] == 1:
                self.results.append(root)
            self.sub_trees[sub_tree] += 1

        return '{} {} {}'.format(left, right, root.val)