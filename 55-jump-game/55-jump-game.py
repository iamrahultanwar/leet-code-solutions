class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # using greedy o(n) | o(1)
        goal = len(nums) - 1
        
        for i in reversed(range(goal)):
            if i + nums[i] >= goal:
                goal = i
                
        return goal == 0
        
            
            
            
        