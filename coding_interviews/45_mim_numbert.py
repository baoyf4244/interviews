import functools
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=functools.cmp_to_key(self.sort_rule))
        return ''.join(nums)

    def sort_rule(self, a, b):
        x = a + b
        y = b + a

        if x > y:
            return 1
        elif x < y:
            return -1
        else:
            return 0
