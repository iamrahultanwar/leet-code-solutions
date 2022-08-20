class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        
        
        def findSum(i,sub,total):
            
            if total == target:
                result.append(sub[::])
                return
            
            if total > target or i >= len(candidates):
                return
            
            total += candidates[i]
            sub.append(candidates[i])
            findSum(i,sub,total)
            sub.pop()
            total -= candidates[i]
            findSum(i+1,sub,total)
            
            
            
        findSum(0,[],0)
        
        return result
                    