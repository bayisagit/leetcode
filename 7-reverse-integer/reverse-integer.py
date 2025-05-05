class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        digit=0
        cons=0
        if x<0:
            x=-1*x
            while x!=0:
                digit=x%10
                cons=cons*10+digit
                x//=10
            result=-1*cons
        elif x>0:
            while x!=0:
                digit=x%10
                cons=cons*10+digit
                x//=10
            result=cons
        if -2147483648 <= result <= 2147483647:
            return result
        else:
            return 0

        