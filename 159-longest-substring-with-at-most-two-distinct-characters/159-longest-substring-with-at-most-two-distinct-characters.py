class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        n = len(s)
        
        if n < 3:
            return n
        
        left,right = 0,0
        
        
        hashMap = defaultdict()
        
        maxLength = 2
        
        while right < n:
            
            hashMap[s[right]] = right
            right += 1
            
            
            if len(hashMap) == 3:
                
                removeIdx = min(hashMap.values())
                
                del hashMap[s[removeIdx]]
                
                left = removeIdx + 1
                
            maxLength = max(maxLength,right - left)
            
        return maxLength 
            