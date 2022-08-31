class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        result = nums[0]
        
        
        maxSum,minSum = 1,1
        
        
        for n in nums:
            temp = maxSum * n
            
            maxSum = max(maxSum*n,minSum*n,n)
            minSum = min(temp,minSum*n,n)
            
            result = max(result,maxSum)
            
            
        return result
            
        