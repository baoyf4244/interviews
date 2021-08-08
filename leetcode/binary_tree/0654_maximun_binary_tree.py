# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums, low, high):
        if not nums:
            return

        if low > high:
            return None

        index = 0
        m = nums[low]
        for i in range(low, high + 1):
            if nums[i] > m:
                m = nums[i]
                index = i

        root = TreeNode(m)
        root.left = self.build(nums, low, index - 1)
        root.right = self.build(nums, index + 1, high)

        return root