class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        start = 0
        max_len = 1
        for right in range(len(s)):
            for left in range(right):
                if s[left] != s[right]:
                    continue

                if left == right:
                    dp[left][right] = True
                elif right - left <= 2:
                    dp[left][right] = True
                else:
                    dp[left][right] = dp[left + 1][right - 1]

                length = right - left + 1
                if dp[left][right] and length > max_len:
                    max_len = length
                    start = left
        return s[start: start + max_len]
