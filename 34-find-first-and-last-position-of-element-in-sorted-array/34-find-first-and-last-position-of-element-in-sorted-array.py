class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left,right = 0,len(nums)-1
        result = [-1,-1]
        
        while left <= right:
            mid = (left + right) // 2
            
            curr = nums[mid]
            
            if curr < target:
                left += 1
            elif curr > target:
                right -= 1
            else:
                result = [mid,mid]
                i,j = mid-1,mid+1
                
                while i >= 0 and nums[i] == target:
                    result[0] = i
                    i -= 1
                    
                while j < len(nums) and nums[j] == target:
                    result[1] = j
                    j += 1
                    
                return result
                
                    
                
            
            
        return result