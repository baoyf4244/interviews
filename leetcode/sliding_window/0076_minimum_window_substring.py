import sys
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        start = 0
        valid = 0
        min_len = sys.maxsize

        need = Counter(t)
        window = Counter()

        while right < len(s):
            c = s[right]
            if c in need:
                window[c] += 1

                if window[c] == need[c]:
                    valid += 1

            right += 1

            while valid == len(need):
                c = s[left]
                if right - left < min_len:
                    start = left
                    min_len = right - left
                if c in need:
                    if need[c] == window[c]:
                        valid -= 1
                    window[c] -= 1

                left += 1
        return s[start: start + min_len] if min_len != sys.maxsize else ''


print(Solution().minWindow('ab', 'a'))

