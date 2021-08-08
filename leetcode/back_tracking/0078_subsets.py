from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        self.back_track(nums, 0, path, res)
        return res

    def back_track(self, nums, start, path, res):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.back_track(nums, i + 1, path, res)
            path.pop()
