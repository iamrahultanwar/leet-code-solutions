class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [-1] * (len(s))
        
        def f(start,wordDict):           
            if start == len(s):
                return True
            
            if dp[start] != -1:
                return dp[start]
            
            for end in range(start+1,len(s)+1):
                
                if s[start:end] in wordDict and f(end, wordDict):
                    dp[start] = True
                    return dp[start]
            
            dp[start] = False
            return dp[start]
        
        
        return f(0,frozenset(wordDict))
                
        