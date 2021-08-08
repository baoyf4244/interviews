from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = []
        self.dfs(n, n, '', res)
        return res

    def dfs(self, left, right, s, res):
        if left == 0 and right == 0:
            res.append(s)
            return

        if left > 0:
            self.dfs(left - 1, right, s + '(', res)

        if right > 0 and right > left:
            self.dfs(left, right - 1, s + ')', res)

