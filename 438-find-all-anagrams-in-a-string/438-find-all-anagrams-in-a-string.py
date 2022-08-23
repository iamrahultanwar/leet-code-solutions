class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        pCount,sCount = {},{}
        
        for i in range(len(p)):
            pCount[p[i]] = pCount.get(p[i],0) + 1
            sCount[s[i]] = sCount.get(s[i],0) + 1
            
            
        
        result = [0] if pCount == sCount else []
        
        
        l = 0
        
        for r in range(len(p),len(s)):
            sCount[s[r]] = sCount.get(s[r],0) + 1
            sCount[s[l]] -= 1
            
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
                
            l += 1
            if sCount == pCount:
                result.append(l)
        
        
        return result
        
        
        
# time out        
#         pCounter = Counter(p)
        
#         result = []
#         def checkAnagram(string):
#             counter = Counter(string)
#             return pCounter == counter
        
#         l = 0
#         for r in range(len(p)-1,len(s)):
#             if checkAnagram(s[l:r+1]):
#                 result.append(l)
                
#             l += 1
            
            
#         return result