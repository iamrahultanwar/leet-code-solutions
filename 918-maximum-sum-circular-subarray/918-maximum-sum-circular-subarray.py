class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        maxTotal,maxSoFar,minSoFar,minTotal,s = nums[0],nums[0],nums[0],nums[0],nums[0]
        
        for idx in range(1,len(nums)):
            maxSoFar = max(nums[idx],maxSoFar+nums[idx])
            maxTotal = max(maxTotal,maxSoFar)
            
            minSoFar = min(nums[idx],minSoFar+nums[idx])
            minTotal = min(minTotal,minSoFar)
            
            s += nums[idx]
            
            
        if minTotal == s:
            return maxTotal
        
        return max(s-minTotal,maxTotal)
