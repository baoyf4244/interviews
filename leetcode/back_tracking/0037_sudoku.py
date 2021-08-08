from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.back_track(board, 0, 0)

    def back_track(self, board, r, c):
        if c == 9:
            return self.back_track(board, r + 1, 0)

        if r == 9:
            return True

        if board[r][c] != '.':
            return self.back_track(board, r, c + 1)

        for n in range(1, 10):
            if not self.is_valid(board, r, c, str(n)):
                continue
            board[r][c] = str(n)
            if self.back_track(board, r, c + 1):
                return True
            board[r][c] = '.'
        return False

    def is_valid(self, board, r, c, n):
        for i in range(9):
            if board[r][i] == n:
                return False

            if board[i][c] == n:
                return False

            if board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3] == n:
                return False

        return True
