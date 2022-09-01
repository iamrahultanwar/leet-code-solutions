/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    
    result = []
    
    const backtrack = (i,curr=[])=>{
        
        if(i==nums.length){
            result.push([...curr])
            return
        }
        
        curr.push(nums[i])
        backtrack(i+1,curr)
        curr.pop()
        backtrack(i+1,curr)
    }
    
    backtrack(0,[])
    
    return result
    
    
};