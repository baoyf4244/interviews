from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [float('-inf') for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)

