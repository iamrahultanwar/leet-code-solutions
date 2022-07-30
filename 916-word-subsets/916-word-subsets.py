class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        cnt = Counter()
        
        for word in words2:
            cnt |= Counter(word)
            
            
        return [a for a in words1 if not cnt - Counter(a)]
