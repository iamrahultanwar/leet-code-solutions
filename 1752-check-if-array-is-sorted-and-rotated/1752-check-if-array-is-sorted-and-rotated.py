class Solution:
    def check(self, nums: List[int]) -> bool:
        # return sum(nums[i] < nums[i-1] for i in range(len(nums))) <= 1
        
        t = 0
        
        for i in range(len(nums)):
            if nums[i] < nums[i-1]:
                t += 1
                
                
        return t <= 1