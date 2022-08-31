class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        
        
        def backtrack(i,curr,total):
            
            if total == target:
                result.append(curr[::])
                return 
            
            if i >= len(candidates) or total > target:
                return
            
            total += candidates[i]
            curr.append(candidates[i])
            backtrack(i,curr,total)
            total -= candidates[i]
            curr.pop()
            backtrack(i+1,curr,total)
            
            
        backtrack(0,[],0)
            
        return result
                    