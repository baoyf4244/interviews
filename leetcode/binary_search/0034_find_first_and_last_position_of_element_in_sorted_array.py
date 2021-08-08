from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                high = mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        if low == len(nums) or nums[low] != target:
            return [-1, -1]

        lower_bound = high
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                low = mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return [lower_bound, low]


Solution().searchRange([5,7,7,8,8,10], 8)