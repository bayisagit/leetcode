class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n=len(arr)
        if n == 1:
            return 1
        bot,up = 1,1
        maxlen = 1
        for r in range(1,n):
            if arr[r] > arr[r-1]:
                bot = up + 1
                up = 1
            elif arr[r] < arr[r-1]:
                up=bot+1
                bot = 1
            else:
                bot,up = 1,1
            maxlen=max(maxlen,bot,up)
        return maxlen