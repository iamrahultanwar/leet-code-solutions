class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        
        def findSubset(i,sub):
            
            if i == len(nums):
                result.append(sub[::])
                return
            
            sub.append(nums[i])
            findSubset(i+1,sub)
            sub.pop()
            findSubset(i+1,sub)
            
            
        findSubset(0,[])
        
        return result