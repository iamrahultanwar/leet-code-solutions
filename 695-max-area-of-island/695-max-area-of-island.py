class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        visited = set()
        
        def dfs(row,col):
            if row not in range(ROWS) or col not in range(COLS) or grid[row][col] == 0 or (row,col) in visited:
                return 0
            
            visited.add((row,col))
            
            return 1 + dfs(row + 1,col) + dfs(row-1,col) + dfs(row,col+1) + dfs(row,col-1)
                    
        
        area = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area,dfs(r,c))
                
        return area