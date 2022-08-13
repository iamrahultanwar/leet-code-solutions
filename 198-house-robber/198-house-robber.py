class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1->3,1
        # 2->1
        
        #2->9,3,1
        
        rob1,rob2 = 0,0
        
        for n in nums:
            temp = max(rob1+n,rob2)
            rob1 = rob2
            rob2 = temp
            
            
        return rob2
    
        