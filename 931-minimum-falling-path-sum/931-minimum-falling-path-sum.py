class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        m = len(matrix[0])
        
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
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
        
        # for j in range(m):
        #     curr = backtrack(n-1,j)
        #     ans = min(ans,curr)
            
            
        for j in range(m):
            dp[0][j] = matrix[0][j]
            
        for i in range(1,n):
            for j in range(m):
                up = matrix[i][j] + dp[i-1][j];
            
                leftDiagonal= matrix[i][j]
                if j-1>=0: leftDiagonal += dp[i-1][j-1]
                else: leftDiagonal += float("inf")

                rightDiagonal = matrix[i][j]
                if j+1<m: rightDiagonal += dp[i-1][j+1]
                else: rightDiagonal += float("inf")

                dp[i][j] = min(up,leftDiagonal,rightDiagonal);
                
        mini = dp[n-1][0]
        
        for j in range(1,m):
            mini = min(mini,dp[n-1][j])

        return mini