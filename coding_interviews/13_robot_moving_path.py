class Solution:
    def __init__(self):
        self.count = 0
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[False for _ in range(n)] for _ in range(m)]
        self.dfs(visited, 0, 0, m, n, k)
        return self.count

    def dfs(self, visited, row, col, m, n, k):
        if 0 <= row < m and 0 <= col < n and not visited[row][col] and self.count_num(col) + self.count_num(row) <= k:
            self.count += 1
            visited[row][col] = True
            for d in self.directions:
                self.dfs(visited, row + d[0], col + d[1], m, n, k)

    def count_num(self, m):
        count = 0
        while m != 0:
            count += m % 10
            m = m // 10

        return count


print(Solution().movingCount(1, 2, 1))