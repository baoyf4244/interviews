from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        track = [['.' for _ in range(n)] for _ in range(n)]
        self.back_tracking(res, track, 0)
        return res

    def back_tracking(self, res, track, r):
        if r == len(track):
            res.append([''.join(t) for t in track])
            return

        for i in range(0, len(track)):
            if not self.is_valid(track, r, i):
                continue

            track[r][i] = 'Q'
            self.back_tracking(res, track, r + 1)
            track[r][i] = '.'

    def is_valid(self, track, r, c):
        for i in range(len(track)):
            if track[i][c] == 'Q':
                return False

        i = r - 1
        j = c - 1
        while i >= 0 and j >= 0:
            if track[i][j] == 'Q':
                return False
            j -= 1
            i -= 1

        i = r - 1
        j = c + 1
        while i >= 0 and j < len(track):
            if track[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True


res = Solution().solveNQueens(4)
print(res)