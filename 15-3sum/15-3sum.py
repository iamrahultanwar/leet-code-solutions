class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        # [-4,-1,-1,0,1,2]
        
        for i,num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
                
            left,right = i+1,len(nums)-1
            
            while left < right:
                
                target = num + nums[left] + nums[right]
                
                if target < 0:
                    left += 1
                elif target > 0:
                    right -= 1
                    
                else:
                    result.append([num,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                        
        return result
            