class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        low = 0
        high = x
        while low <= high:
            mid = low + (high - low) // 2
            sq = x // mid
            if sq == mid:
                return mid
            elif sq > mid:
                low = mid + 1
            else:
                high = mid - 1
        return high
