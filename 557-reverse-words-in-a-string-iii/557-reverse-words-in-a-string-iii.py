class Solution:
    def reverseWords(self, s: str) -> str:
        
        string = s.split(" ")
        
        result = ""
        
        for word in string:
            for st in reversed(word):
                result += st
                
            result += " "
                
        result = result.strip()
            
        return result
            