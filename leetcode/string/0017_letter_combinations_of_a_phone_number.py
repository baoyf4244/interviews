from typing import List


class Solution:
    def __init__(self):
        self.digit2char = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        if len(digits) == 0:
            return list(self.digit2char[digits[0]])

        res = []
        s = ''
        self.dfs(res, s, digits, 0)
        return res

    def dfs(self, res, s, digits, index):
        if index == len(digits):
            res.append(s)
            return  

        num = digits[index]
        letter = self.digit2char[num]
        for c in letter:
            self.dfs(res, s + c, digits, index + 1)


