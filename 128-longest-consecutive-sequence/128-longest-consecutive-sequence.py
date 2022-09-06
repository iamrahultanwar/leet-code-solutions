class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        
        result = 0 
        
        
        for num in nums:
            if (num-1) not in numbers:
                length = 0
                
                while (num+length) in numbers:
                    length += 1
                    
                result = max(result,length)
                
        return result
                