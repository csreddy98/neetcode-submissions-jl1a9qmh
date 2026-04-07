class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = x
        for _ in range(abs(n)-1):
            res *= x
        if n == 0:
            return 1
        if n < 0:
            return 1/res
        else:
            return res