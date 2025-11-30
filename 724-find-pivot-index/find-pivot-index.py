from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        total = prefix[-1]

        for i in range(len(nums)):
            left = prefix[i] - nums[i]     
            right = total - prefix[i]      
            if left == right:
                return i

        return -1
