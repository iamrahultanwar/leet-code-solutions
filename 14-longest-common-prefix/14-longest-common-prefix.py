class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        smallestStr = strs[0]
        
        for s in strs:
            if len(s) < len(smallestStr):
                smallestStr = s
            
        i = 0
        
        while i < len(smallestStr):
            curr = smallestStr[i]
            
            for st in strs:
                if curr != st[i]:
                    return smallestStr[:i]
                
            i += 1
            
        return smallestStr[:i]
                
            
        