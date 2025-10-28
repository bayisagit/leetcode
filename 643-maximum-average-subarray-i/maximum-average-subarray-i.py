class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum = sum(nums[:k])
        currsum = maxsum
        for i in range(k,len(nums)):
            currsum = currsum - nums[i-k] + nums[i]
            maxsum = max(maxsum,currsum)
        return maxsum/k
