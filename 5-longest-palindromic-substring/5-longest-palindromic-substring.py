class Solution(object):
    def longestPalindrome(self, s):
        # handle base case
        
        if len(s)==1:
            return s
        
        
        maxString = ""
        
        
        # idea 
        
        for i in range(len(s)-1):
            for j in range(i,len(s)):
                if s[i] == s[j]:
                    sub = s[i:j+1]
                    if len(sub) > len(maxString):
                        if sub == sub[::-1]:
                            maxString = sub
        
        if len(maxString) ==1:
            return maxString[0]
        
        return maxString

        

 
