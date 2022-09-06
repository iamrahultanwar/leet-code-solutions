class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        Sum = 0
        n = len(nums)
        
        
        for i in range(n):
            Min = nums[i]
            Max = nums[i]
            
            for j in range(i,n):
                Min = min(Min,nums[j])
                Max = max(Max,nums[j])
                
                Sum += Max - Min
                
        
        return Sum
        