class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
            
        
        result = []
        
        
        def dfs(i,part):
            
            if len(part) == k:
                result.append(part[::])

            
            for j in range(i,n+1):

                part.append(j)

                dfs(j+1,part)

                part.pop()


            
            
        dfs(1,[])
        
        return result
            
            
            