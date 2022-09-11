class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sumHash = defaultdict(int)
        sumHash[0] = 1
        count = 0
        total = 0
        for num in nums:         
            total += num
            x = total - k
                    
            if x in sumHash:
                count += sumHash[x]
                
                
            sumHash[total] += 1
            
            
        return count