class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        if not s:
            return True
        while t and s:
            if t[-1] == s[-1]:
                s.pop()
            t.pop()
            
            
        return len(s) == 0