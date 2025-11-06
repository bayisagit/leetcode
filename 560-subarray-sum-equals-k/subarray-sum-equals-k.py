class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        varst = {0:1}
        count=prsum=0
        for num in nums:
            prsum+=num
            if prsum-k in varst:
                count+=varst[prsum-k]
            varst[prsum] = varst.get(prsum,0)+1
        return count