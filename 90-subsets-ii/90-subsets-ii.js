/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    
    result = []
    
    nums.sort()
    const backtrack = (i,curr)=>{

        if(i>=nums.length){
            result.push([...curr])
            return
        }
        
        curr.push(nums[i])
        backtrack(i+1,curr)
        
        curr.pop()

        while(i<nums.length && nums[i] == nums[i+1]){
            i += 1
        }
        
        
        backtrack(i+1,curr)
    }
    
    backtrack(0,[])
    
    return result
};