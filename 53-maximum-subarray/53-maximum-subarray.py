class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current, maxResult = 0,nums[0]
        
        for num in nums:
            
            if current < 0:
                current = 0
                
            current += num
                
            maxResult = max(maxResult,current)
            
            
        return maxResult