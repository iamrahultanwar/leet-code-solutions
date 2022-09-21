class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        total = sum(x for x in nums if x % 2 == 0)
        
        result = []
        
        for val,index in queries:
            
            if nums[index] % 2 == 0:total -= nums[index]
            
            nums[index] += val
            
            if nums[index] % 2 == 0:total += nums[index]
                
            result.append(total)
        
        return result

            