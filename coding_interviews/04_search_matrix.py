from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        m = 0
        n = len(matrix[0]) - 1

        while n >= 0 and m < len(matrix):
            if matrix[m][n] == target:
                return True

            if matrix[m][n] > target:
                n -= 1
            else:
                m += 1
        return False


if __name__ == '__main__':
    a = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15]
    ]
    print(Solution().findNumberIn2DArray(a, 3))