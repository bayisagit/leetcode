class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r,curr=0,0,0
        n=len(nums)
        for i in range(n):
            curr+=nums[i]
            while curr>=target:
                if r==0:
                    r=i-l+1
                r=min(r,i-l+1)
                curr -= nums[l]
                l+=1
        return r




        