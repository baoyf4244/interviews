class Solution:
    def replaceSpace(self, s: str) -> str:
        arr = []
        for c in s:
            if c == ' ':
                arr.append('%20')
            else:
                arr.append(c)

        return ''.join(arr)