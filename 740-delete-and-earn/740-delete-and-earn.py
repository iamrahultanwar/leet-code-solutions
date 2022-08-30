class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        counter = Counter(nums)
        
        nums = sorted(set(nums)) # remove duplicates
        
        prev,curr = 0,0
        
        for i in range(len(nums)):
            currVal = nums[i] * counter[nums[i]]
            
            if i > 0 and nums[i] == nums[i-1] + 1:
                temp = curr
                curr = max(currVal+prev,curr)
                prev = temp
            else:
                temp = curr
                curr = currVal + curr
                prev = temp
                
                
        return curr
                
            