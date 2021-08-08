from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for j in range(0, len(matrix[0])):
            dp[0][j] = matrix[0][j]

        for i in range(1, len(matrix)):
            dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + matrix[i][0]
            for j in range(1, len(matrix[0])):
                if j == len(matrix[0]) - 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
        return min(dp[-1])


print(Solution().minFallingPathSum([[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]))