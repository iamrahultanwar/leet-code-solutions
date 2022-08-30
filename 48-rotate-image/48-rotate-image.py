class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        l,r = 0,len(matrix)-1
        
        
        while l < r:
            
            for i in range(r-l):
                top,bottom = l,r
                
                # store topleft in var
                topLeft = matrix[top][l+i]
                
                
                # top left
                
                matrix[top][l+i] = matrix[bottom-i][l]
        
                # bottom left 
            
                matrix[bottom-i][l] = matrix[bottom][r-i]

                
                # bottom right
                
                matrix[bottom][r-i] = matrix[top+i][r]
                
                # top right = 
                
                matrix[top+i][r] = topLeft
                  
            l += 1
            r -= 1
            
            