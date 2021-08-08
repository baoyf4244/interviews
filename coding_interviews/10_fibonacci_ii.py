class Solution:
    def numWays(self, n: int) -> int:
        if n <= 0:
            return 1
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1] % 1000000007