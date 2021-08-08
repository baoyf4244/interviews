from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        track = []
        self.back_tracking(k, n, 0, res, track)
        return res

    def back_tracking(self, k, n, start, res, track):
        if len(track) == k and sum(track) == n:
            res.append(track[:])
            return

        for i in range(start, 9):
            if len(track) == k and sum(track) < n:
                self.back_tracking(k, n, i + 1, res, track)
                continue

            if sum(track) > n:
                break
            track.append(i + 1)
            self.back_tracking(k, n, i + 1, res, track)
            track.pop()


print(Solution().combinationSum3(2, 18))