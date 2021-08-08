from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        points = [1] + nums + [1]
        dp = [[0 for _ in range(len(points))] for _ in range(len(points))]
        for i in range(len(points) - 1, -1, -1):
            for j in range(i + 1, len(points)):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][k] + dp[k][j] + points[i] * points[k] * points[j], dp[i][j])
        return dp[0][len(points) - 1]


Solution().maxCoins([3, 1, 5, 8])
