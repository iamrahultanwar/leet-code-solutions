class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        
        while left <= right:
            
            mid = (left + right) // 2
            
            current = nums[mid]
            
            if current == target:
                return mid
            
            leftValue = nums[left]
            rightValue = nums[right]
            
            # handle left side portion
            if leftValue <= current:
                if target > current or target < leftValue:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            else:
                if target < current or target > rightValue:
                    right = mid - 1
                else:
                    left = mid + 1
                
                
        return -1
               