from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False

        total = sum(nums)
        if total % 2 == 1:
            return False

        half = total // 2
        dp = [[False for _ in range(half + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, half + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        return dp[len(nums)][half]