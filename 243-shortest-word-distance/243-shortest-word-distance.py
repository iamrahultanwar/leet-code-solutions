class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        idx1,idx2 = -1,-1
        
        diff = len(wordsDict)
        
        for idx,val in enumerate(wordsDict):
            
            if val == word1:
                idx1 = idx
            
            if val == word2:
                idx2 = idx
                
            if idx1 != -1 and idx2 != -1:
                diff = min(diff,abs(idx1-idx2))
                    
                    
        return diff