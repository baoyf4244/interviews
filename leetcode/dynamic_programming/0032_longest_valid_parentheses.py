class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0

        dp = [0 for _ in range(len(s))]
        max_len = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i > dp[i - 1] and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 1 - 1] if i - dp[i - 1] - 1 - 1 >= 0 else 0)

            max_len = max(max_len, dp[i])
        return max_len