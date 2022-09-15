class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        result = [[1 for _ in range(row)] for row in range(1,numRows+1)]
        
        
        for i in range(2,numRows):
            for j in range(numRows):
                if j > 0 and j < i:
                    result[i][j] = result[i-1][j] + result[i-1][j-1]
                    
                    
        return result