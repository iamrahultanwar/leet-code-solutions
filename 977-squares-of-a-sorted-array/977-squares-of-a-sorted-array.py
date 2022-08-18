class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left,right = 0,len(nums)-1
        
        result = [0] * len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
                
            result[i] = square * square
                
        return result
        