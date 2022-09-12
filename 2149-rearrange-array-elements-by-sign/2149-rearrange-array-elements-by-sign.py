class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        result = [0] * len(nums)
        
        p = 0
        n = 1
        
        
        for num in nums:
            
            if num > 0:
                result[p] = num
                p += 2
                
            else:
                result[n] = num
                n += 2
                
                
        return result