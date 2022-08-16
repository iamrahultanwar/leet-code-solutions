class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        counter = Counter(s)
        
        
        for idx,letter in enumerate(s):
            if counter[letter] == 1:
                return idx
            
            
        return -1