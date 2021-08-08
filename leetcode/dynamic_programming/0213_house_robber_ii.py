from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_range(nums[1:]), self.rob_range(nums[: len(nums) - 1]))

    def rob_range(self, nums: List[int]) -> int:
        cur = 0
        pre = 0
        for i in range(len(nums) - 1, -1, -1):
            temp = cur
            cur = max(cur, pre + nums[i])
            pre = temp

        return cur