from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low = 0
        high = len(numbers) - 1
        mid = low  # 避免旋转数据旋转部分长度为零的情况
        while numbers[low] >= numbers[high]:
            if high - low == 1:
                mid = high
                break

            mid = low + (high - low) // 2
            if numbers[low] == numbers[mid] == numbers[high]:
                return min(numbers[low: high + 1])

            if numbers[low] <= numbers[mid]:
                low = mid
            elif numbers[mid] <= numbers[high]:
                high = mid
        return numbers[mid]