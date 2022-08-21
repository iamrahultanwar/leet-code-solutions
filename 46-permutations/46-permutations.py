class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
    
        def backtrack(ds,freq):
            
            if len(ds) == len(nums):
                result.append(ds[::])
                return
            
            for i in range(len(nums)):
                if not freq[i]:
                    ds.append(nums[i])
                    freq[i] = True        
                    backtrack(ds,freq)
                    freq[i] = False        
                    ds.pop()
                    
        freq = [False for i in range(len(nums))]
        
        backtrack([],freq)
        
        return result