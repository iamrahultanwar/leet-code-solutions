class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
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