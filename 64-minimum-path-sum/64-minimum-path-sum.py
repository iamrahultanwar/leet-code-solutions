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
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][i] = grid[i][j]
                    
                else:
                    up = down = grid[i][j]              
                    if i > 0 : 
                        up += dp[i-1][j]
                    else:
                        up += float("inf")
                    if j > 0:
                        down += dp[i][j-1]
                    else:
                        down += float("inf")
                        
                    dp[i][j] = min(up,down)
                
        # return backtrack(len(grid)-1,len(grid[0])-1)
        
        return dp[-1][-1]