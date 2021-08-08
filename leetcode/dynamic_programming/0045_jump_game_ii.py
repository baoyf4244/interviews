from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        dp = [len(nums) for _ in range(len(nums))]
        dp[0] = 0
        dp[1] = 1
        for i in range(1, len(dp)):
            for j in range(0, i):
                if nums[j] >= i - j:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]


print(Solution().jump([2, 3, 1, 1, 4]))
