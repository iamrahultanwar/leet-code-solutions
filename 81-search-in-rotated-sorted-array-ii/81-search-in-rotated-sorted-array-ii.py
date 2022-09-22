class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left,right = 0,len(nums)-1
        
        while left <= right:
            
                # shifting to remove duplicate elements
            while left<right and nums[left] == nums[left+1]:
                left+=1
            while left<right and nums[right] == nums[right-1]:
                right-=1
            
            mid = (left + right) // 2
            
            current = nums[mid]
            
            if current == target:
                return True
            
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
                
                
        return False