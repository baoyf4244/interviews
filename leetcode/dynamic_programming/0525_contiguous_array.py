from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dct = {0: -1}
        max_len = 0
        count = 0
        for i in range(len(nums)):
            count += (1 if nums[i] == 1 else -1)
            if count in dct:
                max_len = max(max_len, i - dct[count])
            else:
                dct[count] = i
        return max_len