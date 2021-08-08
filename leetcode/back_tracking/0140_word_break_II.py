from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        path = []
        self.back_tracking(s, set(wordDict), 0, res, path)
        return res

    def back_tracking(self, s, word_dict, start, res, path):
        if len(''.join(path)) == len(s):
            res.append(' '.join(path[:]))
            return

        for i in range(start, len(s)):
            if not s[start: i + 1] in word_dict:
                self.back_tracking(s, word_dict, i + 1, res, path)
                continue

            path.append(s[start: i + 1])
            self.back_tracking(s, word_dict, i + 1, res, path)
            path.pop()