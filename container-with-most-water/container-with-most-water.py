class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height) - 1 
        
        maxArea = float("-inf")
        
        while left < right:         
            maxArea = max(maxArea,min(height[left],height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            elif height[right] <= height[left]:
                right -= 1
            
        return maxArea
            