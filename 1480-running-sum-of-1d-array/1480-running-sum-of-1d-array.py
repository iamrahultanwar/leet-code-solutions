class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return 0
        
        total = nums[0]        
        
        
        
        for idx in range(1,len(nums)):
            total += nums[idx]
            nums[idx] = total
            
            
        return nums
            