/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    
    result = []
    
    
    const backtrack = (i=0,curr=[],total=0)=>{
        
        if(total==target){
            result.push([...curr])
            return
        }
        if(i >= candidates.length || total > target){
            return
        }
        
        total += candidates[i]
        curr.push(candidates[i])
        backtrack(i,curr,total)
        total -= candidates[i]
        curr.pop()
        backtrack(i+1,curr,total)
    }
    
    backtrack()
    return result
};