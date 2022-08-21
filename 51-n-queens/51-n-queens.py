class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posDia = set() # holds positive diagonals
        negDia = set() # holds negative diagonals
        col = set()
        result = []
        
        board = [["."] * n for i in range(n)]
        
        
        def backtrack(r):
            
            if r == n:
                result.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                
                if c in col or (r + c) in posDia or (r - c) in negDia:
                    continue
                    
                posDia.add(r+c)
                negDia.add(r-c)
                col.add(c)
                board[r][c] = "Q"
                backtrack(r+1)
                posDia.remove(r+c)
                negDia.remove(r-c)
                col.remove(c)
                board[r][c] = "."
                
                
        backtrack(0)
        
        return result