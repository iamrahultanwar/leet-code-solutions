class Solution:
    def subsetSumToKTabu(self,n,k,arr):
        dp = [[False for i in range(k+1)] for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = True
            
        if arr[0] <= k: dp[0][arr[0]] = True
        
        for ind in range(1,n):
            for target in range(1,k+1):
                notTake = dp[ind-1][target]
                
                take = False
                
                if arr[ind] <= target:
                    take = dp[ind-1][target-arr[ind]]   
                    
                dp[ind][target] = take or notTake
                
        return dp[-1][k]
    
    def subsetSumToK(self,n, k, arr):  
        a = arr

        dp = [[-1 for _ in range(k+1)] for _ in range(n)]

        def f(idx,target):
            if target == 0:
                return True     
            if idx <= 0:
                return a[idx] == target        

            if dp[idx][target] != -1: return dp[idx][target]

            notTake = f(idx-1,target) 
            take = False

            if target >= a[idx]:
                take = f(idx-1,target-a[idx])

            dp[idx][target] = take or notTake

            return dp[idx][target]

        return f(n-1,k)

    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum(nums)
        
        if target % 2 : return False
        
        target = target // 2
                    
            
        return self.subsetSumToKTabu(len(nums),target,nums)
                