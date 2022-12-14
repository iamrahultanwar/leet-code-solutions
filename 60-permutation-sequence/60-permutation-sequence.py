class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials,nums = [1],['1']
        
        for i in range(1,n):
            factorials.append(factorials[i-1]*i)
            nums.append(str(i+1))
            
        k -= 1 # fit into base
        
        output = []
        
        for i in reversed(range(n)):
            idx = k // factorials[i]
            k -= idx * factorials[i]
            
            
            output.append(nums[idx])
            
            del nums[idx]
            
        return ''.join(output)