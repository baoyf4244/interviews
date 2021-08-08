from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = Counter()

        left = 0
        right = 0
        res = 0

        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right - left)

        return res


print(Solution().lengthOfLongestSubstring('abcabcbb'))