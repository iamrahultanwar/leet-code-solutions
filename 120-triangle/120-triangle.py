class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        def backtrack(i,j):
            if i == n-1: return triangle[i][j]      
            
            if dp[i][j] != -1: return dp[i][j]
            
            down = triangle[i][j] + backtrack(i+1,j)
            downRight = triangle[i][j] + backtrack(i+1,j+1)
            
            dp[i][j] = min(down,downRight)
            return dp[i][j]
        
        for j in range(n):
            dp[n-1][j] = triangle[n-1][j]
        
        for i in reversed(range(n-1)):
            for j in range(i+1):
                down = triangle[i][j] + dp[i+1][j]
                downRight = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down,downRight)
        
        return dp[0][0]
            
            
            