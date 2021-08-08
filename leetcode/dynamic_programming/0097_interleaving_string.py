# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         if len(s1) + len(s2) != len(s3):
#             return False
#
#         dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
#         dp[0][0] = True
#         for i in range(0, len(s1) + 1):
#             for j in range(0, len(s2) + 1):
#                 p = i + j - 1
#                 if i > 0:
#                     dp[i][j] = dp[i][j] or (dp[i - 1][j] and s1[i - 1] == s3[p])
#                 if j > 0:
#                     dp[i][j] = dp[i][j] or (dp[i][j - 1] and s2[j - 1] == s3[p])
#         return dp[-1][-1]

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            if s1[:i] == s3[: i]:
                dp[i][0] = True
        for j in range(len(s2) + 1):
            if s2[:j] == s3[: j]:
                dp[0][j] = True

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                p = i + j - 1
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[p]) or (dp[i][j - 1] and s2[j - 1] == s3[p])
        return dp[-1][-1]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

Solution().isInterleave(s1, s2, s3)