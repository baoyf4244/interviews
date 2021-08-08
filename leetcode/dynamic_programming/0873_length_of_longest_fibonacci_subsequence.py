from typing import List
from collections import defaultdict


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        indices = {k: i for i, k in enumerate(arr)}
        dp = defaultdict(lambda: 2)
        ans = 0
        for i, k in enumerate(arr):
            for j in range(i):
                idx = indices.get(k - arr[j], None)
                if idx is not None and idx < j:
                    dp[(j, i)] = dp[(idx, j)] + 1
                    ans = max(dp[(j, i)], ans)
        print(dp)
        return ans if ans > 2 else 0


print(Solution().lenLongestFibSubseq([1,2,3,4,5,6,7,8]))