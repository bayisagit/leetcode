class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        b=int(math.sqrt(c))
        while a <= b:
            squ = a*a + b*b
            if squ == c:
                return True
            if squ<c:
                a+=1
            else:
                b-=1
        return False

        