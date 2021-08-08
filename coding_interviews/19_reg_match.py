class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        mem = {}

        def dp(i, j):
            if (i, j) in mem:
                return mem[(i, j)]

            if j == len(p):
                return i == len(s)

            first = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j <= len(p) - 2 and p[j + 1] == '*':
                # 1) * 代表取前面0个
                # 2) * 代表取前面多个
                ans = dp(i, j + 2) or (first and dp(i + 1, j))
            else:
                ans = first and dp(i + 1, j + 1)

            mem[(i, j)] = ans

            return ans

        return dp(0, 0)
