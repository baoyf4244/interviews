from typing import List


# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         left = [0 for _ in range(len(nums))]
#         right = [0 for _ in range(len(nums))]
#         for i in range(1, len(nums)):
#             left[i] = left[i - 1] + nums[i - 1]
#
#         for i in range(len(nums) - 2, -1, -1):
#             right[i] = right[i + 1] + nums[i + 1]
#
#         for i in range(len(nums)):
#             if left[i] == right[i]:
#                 return i
#         return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        s = 0
        for i in range(len(nums)):
            if total == 2 * s + nums[i]:
                return i
            s += nums[i]
        return -1
