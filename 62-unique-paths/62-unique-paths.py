class Solution:
    def tabuWithSpace(self,m:int,n:int)->int:
        
        prev = [0] * n
        
        for i in range(m):
            curr = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = 1
                else:
                    up = prev[j] if i > 0 else 0
                    left = curr[j-1] if j > 0 else 0

                    curr[j] = up + left
            
            prev = curr
            
        return prev[-1]
    
    def tabu(self,m:int,n:int)->int:
        return self.tabuWithSpace(m,n)
    
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                up = dp[i-1][j] if i > 0 else 0
                left = dp[i][j-1] if j > 0 else 0
                
                dp[i][j] = up + left
                
                
        return dp[-1][-1]
    
    def uniquePaths(self, m: int, n: int) -> int:
        
        return self.tabu(m,n)
        
        if m == 1 and n == 1:
            return 1
        
        dp = [[-1 for _ in  range(n)] for _ in range(m)]
        
        def backtrack(i,j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            
            if dp[i][j] != -1 : return dp[i][j]
            up = backtrack(i-1,j)
            down = backtrack(i,j-1)
            
            dp[i][j] = up + down
            return dp[i][j]
        
        
        backtrack(m-1,n-1)
        
        return dp[m-1][n-1]