class Solution:
    def reverse(self, x: int) -> int:
                
        counts = 0
        isNegative = True if x < 0 else False
        
        if isNegative:
            x *= -1 
        temp = x

        while x:
            counts += 1      
            x = x//10
        ans = 0
        while temp:
            m = temp % 10
            counts -= 1
            ans += int(m * math.pow(10, counts))
            temp = temp // 10
            
                
        if ans > math.pow(2,31):
            return 0
        
        return ans * -1 if isNegative else ans