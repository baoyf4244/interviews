from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        low = 0
        high = len(nums) - 1

        while low < high:
            if nums[low] % 2 == 0 and nums[high] % 2 == 1:
                nums[low], nums[high] = nums[high], nums[low]

            if nums[low] % 2 == 1:
                low += 1

            if nums[high] % 2 == 0:
                high -= 1

        return nums


