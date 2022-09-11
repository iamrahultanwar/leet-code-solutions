class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        counter = Counter(t)        
        
        for st in s:
            if counter[st] == 0:
                return False
            
            counter[st] -= 1
        
        for val in counter.values():
            if val > 0:
                return False
            
            
        return True