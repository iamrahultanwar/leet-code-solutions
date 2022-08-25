class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s1 = []
        s2 = []
        
        def prepareStack(word,stack):
            for l in word:
                if l == "#":
                     if len(stack) > 0: stack.pop()
                else:
                    stack.append(l)
        
        prepareStack(s,s1)
        prepareStack(t,s2)
        
        
        return s1 == s2