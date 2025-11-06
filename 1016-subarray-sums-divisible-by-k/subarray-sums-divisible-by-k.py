class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_counts = {0: 1}  # remainder 0 initially
        prefix_sum = 0
        count = 0
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            
            # Python can give negative remainders for negative numbers
            if remainder < 0:
                remainder += k
            
            if remainder in prefix_counts:
                count += prefix_counts[remainder]
            
            prefix_counts[remainder] = prefix_counts.get(remainder, 0) + 1
        
        return count
