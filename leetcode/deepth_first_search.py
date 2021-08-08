from typing import List


class Solution:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        max_area = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_area = max(max_area, self.dfs(grid, i, j))

        return max_area

    def dfs(self, grid, r, c):
        if grid[r][c] == 0:
            return 0
        area = 1
        grid[r][c] = 0
        for direction in self.directions:
            n_r = r + direction[0]
            n_c = c + direction[1]
            if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]):
                area += self.dfs(grid, n_r, n_c)
        return area