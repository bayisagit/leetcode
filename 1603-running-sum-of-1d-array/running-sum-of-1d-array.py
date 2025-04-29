class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newnums=[]
        sums=0
        for i in nums:
            sums+=i
            newnums.append(sums)
        return newnums
        