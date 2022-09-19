class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        result = nums[0]
        
        minProduct = 1
        maxProduct = 1
        
        
        for num in nums:
            temp = maxProduct * num
            
            maxProduct = max(maxProduct*num,minProduct*num,num)
            minProduct = min(temp,minProduct*num,num)
            
            result = max(result,maxProduct)
            
            
        return result
            
        