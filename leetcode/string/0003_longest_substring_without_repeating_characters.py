from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        res = 0

        window = Counter()
        while right < len(s):
            c = s[right]
            window[c] += 1
            right += 1
            while window[c] > 1:  # 一直减到与c相同的字符
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right - left)
        return res
