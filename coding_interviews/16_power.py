class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        unsigned_n = abs(n)
        if unsigned_n == n:
            return self.unsighned_pow(x, unsigned_n)
        else:
            return self.unsighned_pow(1 / x, unsigned_n)

    def unsighned_pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x

        half = n // 2
        half_pow = self.unsighned_pow(x, half)
        if n % 2 == 1:
            return half_pow ** 2 * x
        else:
            return half_pow ** 2
