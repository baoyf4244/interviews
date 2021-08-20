from typing import List


class Solution:
    def __init__(self):
        self.results = []
        self.visited = []

    def permutation(self, s: str) -> List[str]:
        self.visited = [False for _ in range(len(s))]
        s_l = list(s)
        s_l.sort()
        self.dfs([], s_l)
        return self.results

    def dfs(self, res, s):
        if len(res) == len(s):
            self.results.append(''.join(res))
            return

        for i in range(len(s)):
            if self.visited[i] or (i > 0 and not self.visited[i - 1] and s[i] == s[i - 1]):
                continue
            res.append(s[i])
            self.visited[i] = True
            self.dfs(res, s)
            self.visited[i] = False
            res.pop()