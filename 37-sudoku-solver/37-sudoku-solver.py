class Solution:
    def isValid(self,board,row,col,c):
        for i in range(9):
            if board[row][i] == c: return False
            if board[i][col] == c: return False
            if board[3 * (row // 3) + (i//3)][3 * (col // 3) + (i%3)] == c: return False
            
        return True
    
    def solve(self,board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                
                if board[row][col] == ".":
                    for c in range(1,10):
                        c = str(c)
                        if self.isValid(board,row,col,c):
                            board[row][col] = c
                            
                            if self.solve(board):
                                return True
                            else:
                                board[row][col] = "."
                    return False
                
        return True
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        return self.solve(board)