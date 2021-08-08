from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for _ in range(len(nums))]
        right = [1 for _ in range(len(nums))]
        answer = []
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]

        print(left)
        print(right)
        for i in range(len(nums)):
            answer.append(left[i] * right[i])

        return answer


print(Solution().productExceptSelf([1,2,3,4]))