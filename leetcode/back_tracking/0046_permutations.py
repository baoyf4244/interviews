from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []
        self.back_track(track, nums)
        return self.res

    def back_track(self, track, nums):
        if len(track) == len(nums):
            self.res.append(track[:])
            return

        for num in nums:
            if num in track:
                continue

            track.append(num)
            self.back_track(track, nums)
            track.pop()