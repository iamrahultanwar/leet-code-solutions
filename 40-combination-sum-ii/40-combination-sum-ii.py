class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        
        result = []
        
        def findSum(i,sub,target):       
            if target == 0:
                result.append(sub[::])
                return            
            if target < 0:
                return
            
            prev = -1
                      
            for j in range(i,len(candidates)):
                if prev == candidates[j]:
                    continue
                    
                sub.append(candidates[j])
                findSum(j+1,sub,target-candidates[j])
                sub.pop()
                
                prev = candidates[j]
                
        findSum(0,[],target)
        
        return result