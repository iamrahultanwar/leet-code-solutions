class Solution:
    # o(n*2**n) | o(n)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()
        def backtrack(i,sub):
            
            if i >= len(nums):
                result.append(sub[::])
                return 
            
            sub.append(nums[i])
            
            backtrack(i+1,sub)
            
            sub.pop()
            
            while i < len(nums) - 1  and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1,sub)
            
            
        backtrack(0,[])
        
        return result
                
        
        
        