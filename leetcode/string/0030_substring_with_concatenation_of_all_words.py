from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return [0]

        counter = Counter(words)
        n = len(words[0])
        for i in range(len(s) - n + 1):
            pass