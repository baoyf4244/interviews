from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()

        left = 0
        right = 0
        valid = 0

        while right < len(s2):
            c = s2[right]
            if c in need:
                window[c] += 1

                if window[c] == need[c]:
                    valid += 1

            right += 1

            if right - left == len(s1):
                if valid == len(need):
                    return True
                c = s2[left]
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
                left += 1

        return False

