class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        
        if n == 1:
            return [i for i in range(10)]
        
        
        result = []
        
        def dfs(n,num):
            
            if n == 0:
                result.append(num)
                return
            
            lastDigit = num % 10
            
            nextDigits = set([lastDigit + k, lastDigit - k])
            
            for nextDigit in nextDigits:
                if 0<= nextDigit < 10:
                    newNum = num * 10 + nextDigit

                    dfs(n-1,newNum)
                    
                    
        for num in range(1,10):
            dfs(n-1,num)
            
        return result