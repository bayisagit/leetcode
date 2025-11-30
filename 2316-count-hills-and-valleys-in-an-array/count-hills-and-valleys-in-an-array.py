class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        a = []
        for x in nums:
            if not a or a[-1] != x:
                a.append(x)
        n = len(nums)
        m = len(a)
        if n < 3:
            return 0
        count = 0
        for i in range(1,m-1):
            if a[i-1] < a[i] and a[i+1] < a[i]:
                count += 1
            elif a[i-1] > a[i] and a[i+1] > a[i]:
                count += 1

        return count