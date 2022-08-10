class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        return nums[-k]
            
        
# 1,2,3,4,5,6 