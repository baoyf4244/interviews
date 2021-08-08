class Solution:
    def numDecodings(self, s: str) -> int:
        dct = {str(k): chr(v) for k, v in zip(range(1, 27), range(65, 65 + 26))}
        if len(s) == 0 or s[0] == '0':
            return 0

        dp = [1 for _ in range(len(s) + 1)]
        for i in range(2, len(s) + 1):
            if s[i - 1] == '0':
                if s[i - 2] == '0':
                    return 0
                if (i == len(s) or i == len(s) - 1) and s[i - 2:] not in dct:
                    return 0

                dp[i] = dp[i - 2]
            else:
                if s[i - 2: i] in dct:
                    dp[i] = dp[i - 2] + dp[i - 1]
                else:
                    dp[i] = dp[i - 1]

        return dp[-1]


print(Solution().numDecodings('301'))