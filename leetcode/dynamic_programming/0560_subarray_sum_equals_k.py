from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        pre = 0
        dct = {0: 1}
        for i, num in enumerate(nums):
            pre += num
            cur = pre - k
            if cur in dct:
                count += dct[cur]
            dct[pre] = dct.get(pre, 0) + 1
        return count
