from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []
        res = []
        track = []
        self.back_tracking(n, n, track, res)
        return res

    def back_tracking(self, left, right, track, res):
        if left < 0 or right < 0:
            return
        if left > right:
            return

        if left == 0 and right == 0:
            res.append(''.join(track))
            return

        track.append('(')
        self.back_tracking(left - 1, right, track, res)
        track.pop()

        track.append(')')
        self.back_tracking(left, right - 1, track, res)
        track.pop()
