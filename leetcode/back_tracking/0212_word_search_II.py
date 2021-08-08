from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        max_len = max(len(word) for word in words)
        res = []
        track = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.back_tracking(board, set(words), max_len, visited, res, track, i, j)
        return res

    def back_tracking(self, board, words, max_len, visited, res, path, r, c):
        word = ''.join(path)
        if word in words:
            res.append(word)

        if len(word) > max_len:
            return

        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            n_r = direction[0] + r
            n_c = direction[1] + c
            if n_r < 0 or n_r >= len(board) or n_c < 0 or n_c >= len(board[0]) or visited[n_r][n_c]:
                continue

            path.append(board[n_r][n_c])
            visited[r][c] = True
            self.back_tracking(board, words, max_len, visited, res, path, n_r, n_c)
            path.pop()
            visited[r][c] = False


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
print(Solution().findWords(board, words))
