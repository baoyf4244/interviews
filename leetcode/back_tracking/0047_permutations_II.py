from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        visited = [False for _ in range(len(nums))]
        self.back_tracking(res, path, nums, visited)
        return res

    def back_tracking(self, res, path, nums, visited):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                continue

            path.append(nums[i])
            visited[i] = True
            self.back_tracking(res, path, nums, visited)
            visited[i] = False
            path.pop()