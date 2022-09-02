class Solution:
    def stringToNum(self,string):
        digit = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            
        }
        num = digit[string[-1]]
        for idx,s in enumerate(reversed(string[:len(string)-1])):
            num  += digit[s] * (10**(idx+1))
        
        return num

    def multiply(self, num1: str, num2: str) -> str:
        
        num1 = self.stringToNum(num1)
        num2 = self.stringToNum(num2)
        
        return str(num1 * num2)