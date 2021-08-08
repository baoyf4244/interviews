from typing import List
from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        indices = {k: i for i, k in enumerate(A)}
        dp = defaultdict(lambda: 2)
        ans = 0
        for k in range(len(A)):
            for j in range(k):
                i = indices.get(2 * A[j] - A[k], None)
                if i is not None and i < j:
                    dp[(j, k)] = dp[(i, j)] + 1
                    ans = max(ans, dp[(j, k)])
        print(dp)
        return max(ans)


print(Solution().longestArithSeqLength([44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28]))