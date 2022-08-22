class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isValid(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
            
        result = []
        
        def backtrack(i,part):
            if i >= len(s):
                result.append(part.copy())
                return
            for j in range(i, len(s)):
                if isValid(i, j):
                    part.append(s[i : j + 1])
                    backtrack(j + 1,part)
                    part.pop()
                    
        backtrack(0,[])
        
        return result