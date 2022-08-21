class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0
        
        
        for r in range(len(s)): # loop over the string to
            while s[r] in charSet: # we have found a duplicate 
                charSet.remove(s[l]) # shrink the window
                l += 1
                
            charSet.add(s[r])
            
            res = max(res,r - l + 1)
            
            
        return res