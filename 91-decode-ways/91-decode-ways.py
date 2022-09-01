class Solution:
    def numDecodings(self, s: str) -> int:
                
        
        dp = [-1] * len(s)
        
        def backtrack(i):       
            if i == len(s): # if i matches the len of s which means we are at the end of the string
                return 1
            
            if s[i] == '0':
                return 0 # we can not have str with 0 as starting point
            
            
            if i == len(s)-1:
                return 1 # check if we can proceed further 
            
            if dp[i] != -1:
                return dp[i]
            
            ans = backtrack(i+1) # check for next char
            
            if int(s[i:i+2]) <= 26: # check for next two char
                ans  += backtrack(i+2)
                
            dp[i] = ans
            return ans
            
            
        return backtrack(0)