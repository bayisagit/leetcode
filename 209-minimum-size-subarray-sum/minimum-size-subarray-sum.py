class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minilength = 0
        l,r=0,0
        totalsum = 0
        for i in range(len(nums)):
            totalsum += nums[i]
            while totalsum >= target:
                if r == 0:
                    r = i - l + 1
                r = min(r,i-l+1)
                totalsum -= nums[l]
                l += 1
                
        return r


        