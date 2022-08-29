class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        
        dp = [-1] * (n + 1)
        def backtrack(i):
            if i == 0:
                return 0
            if i <= 2:
                return 1
            if dp[i] != -1:return dp[i]            
            dp[i] = backtrack(i-1) + backtrack(i-2) + backtrack(i-3)
            return dp[i]
        
        backtrack(n)
        
        return dp[n]
    
    
    
    # tn = tn3 - tn2 - tn1