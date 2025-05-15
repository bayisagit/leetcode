class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(x, n):
            if n == 0:
                return 1
            half = rec(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        
        return rec(x, n) if n >= 0 else 1 / rec(x, -n)
