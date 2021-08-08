from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            if matrix[i][0] == '1':
                dp[i][0] = 1

        for j in range(len(matrix[0])):
            if matrix[0][j] == '1':
                dp[0][j] = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

        max_side = max([max(dp[i]) for i in range(len(matrix))])
        return max_side * max_side

