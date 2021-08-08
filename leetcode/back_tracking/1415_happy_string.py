class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        path = []
        self.back_tracking(n, res, path)
        res.sort()
        print(res)
        return res[k - 1] if k - 1 < len(res) else ''

    def back_tracking(self, n, res, path):
        if len(path) == n:
            res.append(''.join(path))
            return

        for alpha in ['a', 'b', 'c']:
            if not self.is_happy_string(path, alpha):
                continue

            path.append(alpha)
            self.back_tracking(n, res, path)
            path.pop()

    def is_happy_string(self, path, alpha):
        if path:
            if path[-1] == alpha:
                return False
        return True


print(Solution().getHappyString(1, 3))