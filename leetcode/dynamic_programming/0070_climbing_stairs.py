# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [1 for _ in range(n + 1)]
#         for i in range(2, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]
#
#         return dp[-1]



class Solution:
    def climbStairs(self, n: int) -> int:
        dp_2 = 1
        dp_1 = 1
        dp = 1
        for i in range(2, n + 1):
            dp = dp_1 + dp_2
            dp_2 = dp_1
            dp_1 = dp

        return dp