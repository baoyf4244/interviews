from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == i:  # nums[i]：索引i的实际元素， i：索引i的正确元素
                continue

            if nums[nums[i]] == nums[i]:  # 索引nums[i]指向的元素是否等于nums[i]
                return nums[i]

            # temp = nums[nums[i]]
            # nums[nums[i]] = nums[i]
            # nums[i] = temp
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]  # 顺序不可颠倒

        return -1