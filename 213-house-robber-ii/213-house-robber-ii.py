class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 1:return nums[0]
        
        def backtrack(i,array,dp):
            if i >= len(array):
                return 0   
            if dp[i] != -1:return dp[i]
            
            take = array[i] + backtrack(i+2,array,dp)
            notTake = 0 + backtrack(i+1,array,dp)
            dp[i] = max(take,notTake)
            return dp[i]
        
        
        dp1, dp2 = [-1 for _ in range(n)],[-1 for _ in range(n)]
        
        return max(backtrack(0,nums[:n-1],dp1),backtrack(0,nums[1:],dp2))