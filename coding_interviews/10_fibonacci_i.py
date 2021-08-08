class Solution:
    def __init__(self):
        self.mem = {}

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if n in self.mem:
            return self.mem[n]

        f = self.fib(n - 1) + self.fib(n - 2)
        self.mem[n] = f
        return f % 1000000007
