from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        results = []
        for i in range(m):
            for j in range(n):
                results.append(matrix[i][j])