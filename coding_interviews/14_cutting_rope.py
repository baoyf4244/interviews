class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        dp = [1 for _ in range(n + 1)]
        dp[0] = 0
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n + 1):
            dp[i] = i - 1
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], dp[j] * dp[i - j])
        print(dp)
        return dp[-1]


print(Solution().cuttingRope(10))