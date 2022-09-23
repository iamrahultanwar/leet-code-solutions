MOD = 10**9 + 7

class Solution:
    def convertToBinary(self,num):
        return bin(num).replace("0b", "")
    
    def convertToDecimal(self,binary):
        return int(binary,2) % MOD
        
    def concatenatedBinary(self, n: int) -> int:
        binary = ""
        for i in range(1,n+1):
            binary += self.convertToBinary(i)
        
        return self.convertToDecimal(binary)