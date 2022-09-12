class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        result = []
        
        p = []
        n = []
        
        for num in nums:
            if num > 0:
                p.append(num)
            else:
                n.append(num)
                
                
        for i in range(len(nums)//2):
            result.append(p[i])
            result.append(n[i])          
            
            
        return result