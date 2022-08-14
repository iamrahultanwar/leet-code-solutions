class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        isLandsCount = 0
        
        visited = set()
        
        def bfs(row,col):
            q = deque()
            q.append((row,col))
            visited.add((row,col))
            
            while q:
                r,c = q.popleft()
                directions = [(1,0),(-1,0),(0,1),(0,-1)]    
                for dr,dc in directions:
                    rr,cc = r+dr, c+dc
                    if rr in range(len(grid)) and cc in range(len(grid[0])) and (rr,cc) not in visited and grid[rr][cc] == "1":
                        q.append((rr,cc))
                        visited.add((rr,cc))
                    
                    
        
        
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):            
                if grid[row][col] == "1" and (row,col) not in visited:
                    bfs(row,col)
                    isLandsCount += 1
                                        
                        
                        
                        
        return isLandsCount