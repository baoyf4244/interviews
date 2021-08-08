class SolutionSimple:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()

        def dp(k, n):
            if n == 0:
                return 0
            if k == 1:
                return n

            if (k, n) in memo:
                return memo[(k, n)]

            res = float('inf')
            for i in range(1, n + 1):
                res = min(res, max(dp(k, n - i), dp(k - 1, i - 1)) + 1)

            memo[(k, n)] = res
            return res

        return dp(K, N)


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
        m = 0
        while dp[K][m] < N:
            m += 1
            for i in range(1, K + 1):
                dp[i][m] = dp[i][m - 1] + dp[i - 1][m - 1] + 1

        return m