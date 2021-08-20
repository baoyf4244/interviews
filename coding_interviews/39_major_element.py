from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct = {}
        half_len = len(nums) / 2
        for num in nums:
            if num not in dct:
                dct[num] = 1
            else:
                dct[num] += 1
            if dct[num] > half_len:
                return num
        return 0
