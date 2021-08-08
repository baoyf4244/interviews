from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [0 for _ in range(len(nums))]
        dp_min = [0 for _ in range(len(nums))]
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                dp_max[i - 1], dp_min[i - 1] = dp_min[i - 1], dp_max[i - 1]
            dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i])
            dp_min[i] = min(dp_min[i - 1] * nums[i], nums[i])
            res = max(res, dp_max[i])
        return res


Solution().maxProduct([2,3,-2,4])