class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max((i - j) * j, dp[i - j] * j, dp[i])
        return dp[-1]