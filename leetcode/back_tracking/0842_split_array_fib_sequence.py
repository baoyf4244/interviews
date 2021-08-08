from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        path = []
        res = []
        self.back_tracking(S, 0, path)

    def back_tracking(self, s, start, path):
        if start == len(s):
            return True

        for i in range(start, len(s)):
            path