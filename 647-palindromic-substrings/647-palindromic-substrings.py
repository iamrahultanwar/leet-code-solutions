class Solution:
    def countSubstrings(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        result = 0
        
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):                
                if s[i] == s[j]:
                    sub = s[i:j+1]
                    if sub == sub[::-1]:
                        result += 1
                        
                        
        
        return result + len(s)