class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        nums=[]
        if num%3!=0:
            return []
        resu=num//3
        return [resu-1,resu,resu+1]