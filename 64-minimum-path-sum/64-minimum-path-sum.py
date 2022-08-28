class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp = [[-1 for col in row] for row in grid]
        
        def backtrack(i,j):      
            if i == 0 and j == 0:
                return grid[i][j]
            if i < 0 or j < 0:
                return float("inf")
            
            if dp[i][j] != -1: return dp[i][j]
    
            up = grid[i][j] + backtrack(i-1,j)
            down = grid[i][j] + backtrack(i,j-1)
            
            dp[i][j] = min(up,down)
            return dp[i][j]

        return backtrack(len(grid)-1,len(grid[0])-1)