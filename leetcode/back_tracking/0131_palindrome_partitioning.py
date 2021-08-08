from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        self.back_tracking(s, 0, len(s), res, path)
        return res

    def back_tracking(self, s, start, l, res, path):
        if l == 0:
            res.append(path[:])
            return

        for i in range(start, len(s)):
            if not self.is_palindrome(s[start: i + 1]):
                continue

            path.append(s[start: i + 1])
            self.back_tracking(s, i + 1, l - len(s[start: i + 1]), res, path)
            path.pop()

    def is_palindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


print(Solution().partition('aab'))
