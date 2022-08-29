class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        m = len(matrix[0])
        
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        
        def backtrack(i,j):           
            if j < 0 or j >= m:
                return float("inf")
            
            if i==0:return matrix[i][j]
            
            if dp[i][j] != -1: return dp[i][j]
            
            up = matrix[i][j] + backtrack(i-1,j)
            upLeft = matrix[i][j] + backtrack(i-1,j-1) 
            upRight = matrix[i][j] + backtrack(i-1,j+1)
            
            dp[i][j] = min(up,upLeft,upRight)
            return dp[i][j]
        
        ans = float("inf")
        
        for j in range(m):
            curr = backtrack(n-1,j)
            ans = min(ans,curr)
            
            
        return ans