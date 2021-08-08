from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda i: i[1])
        count = 0
        prev = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev:
                count += 1
            else:
                prev = intervals[i][1]
        return count