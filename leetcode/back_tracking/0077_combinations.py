from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        self.back_track(n, k, 1, path, res)
        return res

    def back_track(self, n, k, start, path, res):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            self.back_track(n, k, i + 1, path, res)
            path.pop()