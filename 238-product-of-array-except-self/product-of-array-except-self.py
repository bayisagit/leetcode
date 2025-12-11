class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefixmult = [1] * n
        prefixmult[0] = nums[0]
        postfixmult = [1] * n
        postfixmult[n-1] = nums[n-1]
        for i in range(1,n):
            prefixmult[i] = prefixmult[i-1] * nums[i]
        for j in range(n-2,-1,-1):
            postfixmult[j] = postfixmult[j+1] * nums[j]
        finalresu = [1] * n
        for k in range(n):
            if k == 0:
                finalresu[k] = postfixmult[k+1]
            elif k == n-1:
                finalresu[k] = prefixmult[k-1]
            else:
                finalresu[k] = prefixmult[k-1] * postfixmult[k+1]
        return finalresu
        
