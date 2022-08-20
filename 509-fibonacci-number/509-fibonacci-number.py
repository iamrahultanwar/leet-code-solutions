class Solution:
    def fib(self, n: int) -> int:
        prev1,prev2 = 1,0
                
        if n <= 1:
            return n

        for i in range(2,n+1):
            temp = prev1
            prev1 = prev1 + prev2
            prev2 = temp
            
        return prev1