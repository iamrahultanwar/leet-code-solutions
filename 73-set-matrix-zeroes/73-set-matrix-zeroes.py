class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ROWS,COLS = len(matrix),len(matrix[0])
        
        
        def dfs(r,c):
            for row in range(r+1,ROWS):
                matrix[row][c] = 0
            
            for row in range(r):
                matrix[row][c] = 0
                
            for col in range(c+1,COLS):
                matrix[r][col] = 0
                
            for col in range(c):
                matrix[r][col] = 0
            
        zeros = []
        
        
        
        for r in range(ROWS):
            for c in range(COLS):         
                if matrix[r][c] == 0:
                    zeros.append((r,c))
                    
                    
        while zeros:
            row,col =  zeros.pop()
            dfs(row,col)
        
                    
                    
        return matrix
    
    
    
    [[0,1,2,0],
     [3,4,5,2],
     [1,3,1,5]]
