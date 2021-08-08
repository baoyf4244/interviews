class Solution:
    def __init__(self):
        self.count = 0

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        track = set()
        self.back_tracking(n, track, n)
        return self.count

    def back_tracking(self, n, track, left):
        if left == 0:
            self.count += 1
            return

        for i in range(10):
            if len(track) == 0 and i == 0:
                self.back_tracking(n, track, left - 1)
                continue
            if i in track:
                continue

            track.add(i)
            self.back_tracking(n, track, left - 1)
            track.remove(i)


print(Solution().countNumbersWithUniqueDigits(2))