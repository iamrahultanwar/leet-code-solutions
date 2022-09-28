class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left,right = 1,max(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            currSum = 0
            
            for num in nums:
                currSum += ceil(num/mid)
                
            
            if currSum <= threshold:
                right = mid
                
            else:
                left = mid + 1
                
                
        return right