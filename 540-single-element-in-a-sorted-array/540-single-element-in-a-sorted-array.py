class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        left,right = 0,len(nums)-1
        
        while left < right:
            mid = left + (right - left) // 2
            
            isEven = (right - mid) % 2 == 0
            
            if nums[mid+1] == nums[mid]:
                if isEven:
                    left = mid + 2
                else:
                    right = mid - 1
                    
            elif nums[mid-1] == nums[mid]:
                if isEven:
                    right = mid -2
                else:
                    left = mid + 1
                    
            else:
                return nums[mid]
            
        return nums[left]
                