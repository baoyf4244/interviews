class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s_list = list(s)
        stack = []

        l = len(s_list)
        i = 0
        while i < l:
            if i == 0 or s_list[i - 1] != s_list[i]:
                stack.append(1)
            else:
                increment = stack.pop() + 1
                if increment == k:
                    for _ in range(k):
                        del s_list[i - k + 1]
                    i = i - k
                else:
                    stack.append(increment)
            i += 1
            l = len(s_list)
        return ''.join(s_list)


# print(Solution().removeDuplicates("pbbcggttciiippooaais",  2))
print(12 + 10 + 21 + 18 + 23 + 11 + 10 + 23)
print(11 + 18 + 22 + 10 + 24 + 27 + 11 + 20 + 8 + 10 + 9 + 9 + 7 + 7 + 10 + 12 + 13 + 12 + 12 + 18 + 16 + 16 + 7 + 5 + 18 + 12 + 9 + 12 + 7 + 14 + 11 + 8 + 9 + 5 + 13 + 14 + 12)
print(len('11 + 18 + 22 + 10 + 24 + 27 + 11 + 20 + 8 + 10 + 9 + 9 + 7 + 7 + 10 + 12 + 13 + 12 + 12 + 18 + 16 + 16 + 7 + 5 + 18 + 12 + 9 + 12 + 7 + 14 + 11 + 8 + 9 + 5 + 13 + 14 + 12'.split('+')))