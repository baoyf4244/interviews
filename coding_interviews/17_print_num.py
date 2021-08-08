from typing import List


class Solution:
    def __init__(self):
        self.start = 0
        self.nine = 0
        self.results = []

    def printNumbers(self, n: int) -> List[int]:
        self.start = n - 1
        s = ['0'] * n
        self.dfs(n, 0, s)
        return self.results

    def dfs(self, n, x, s):
        if n == x:
            num = int(''.join(s[self.start:]))
            if num != 0:
                self.results.append(num)
            if n - self.start == self.nine:
                self.start -= 1
            return

        for i in range(10):
            if i == 9:
                self.nine += 1
            s[x] = str(i)
            self.dfs(n, x + 1, s)
        self.nine -= 1


Solution().printNumbers(1)