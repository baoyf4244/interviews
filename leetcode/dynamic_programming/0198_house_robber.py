from typing import List


class SimpleSolution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums) + 2)]
        for i in range(len(nums) - 1, -1, -1):
            dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
        return dp[0]


class Solution:
    def rob(self, nums: List[int]) -> int:
        cur = 0
        pre = 0
        for i in range(len(nums) - 1, -1, -1):
            temp = cur
            cur = max(cur, pre + nums[i])
            pre = temp

        return cur