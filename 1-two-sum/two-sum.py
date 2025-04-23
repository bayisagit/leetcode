class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict()

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in dic:
                return [dic[temp], i]
            else:
                dic[nums[i]] = i


        
        