class Solution:
    def dpWithMemo(self,nums:List[int]) -> int:
        
        dp = [-1] * len(nums)
        
        maxNumber = [-1]
        
        def backtrack(i):
            
            if i >= len(nums):
                return 0
            
            if dp[i] > -1 : return dp[i]
            
            take = backtrack(i+2) + nums[i]
            notTake = backtrack(i+1)
            
            dp[i] = max(take,notTake)
            
            maxNumber[0] = max(maxNumber[0],dp[i])
            return dp[i]
        
        backtrack(0)
        
        return maxNumber[0]
    
    def dpWithTabu(self,nums:List[int]) -> int:
        
        rob1,rob2 = 0,0 # rob1 is take and rob2 is not take
        
        for n in nums:
            temp = max(rob1+n,rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
        
    def rob(self, nums: List[int]) -> int:
        
        return self.dpWithMemo(nums)
        # 1->3,1
        # 2->1
        
        #2->9,3,1
        
#         rob1,rob2 = 0,0
        
#         for n in nums:
#             temp = max(rob1+n,rob2)
#             rob1 = rob2
#             rob2 = temp
            
            
#         return rob2
    
        
        
        # [1,2,3,1]