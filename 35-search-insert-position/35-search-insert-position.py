class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l,r = 0,len(nums)-1
        
        
        while l <= r:
            mid = (l+r) // 2
            
            curr = nums[mid]
            
            if curr == target:
                return mid
            
            if target < curr:
                r = mid - 1
            else:
                l = mid + 1

                
        return l
                
        
        