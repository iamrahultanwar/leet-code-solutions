# o(n^2) | o(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = [1] * len(nums)
    
    
        for i in reversed(range(len(nums))):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    result[i] = max(result[i],1+result[j])
                    
        return max(result)

                    
            
        