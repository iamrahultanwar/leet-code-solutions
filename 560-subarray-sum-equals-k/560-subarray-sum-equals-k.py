class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumHash = {}
        
        count,sum_ = 0,0
        
        sumHash[0] = 1
        
        for n in nums: 
            sum_ += n
            
            if (sum_ - k) in sumHash:
                count += sumHash[sum_-k]
                
                
            sumHash[sum_] = sumHash.get(sum_,0) + 1
            
            
        return count