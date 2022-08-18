class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        
        
        while left < right:
            x = numbers[right] + numbers[left]
            
            if x > target:
                right -= 1
                
            elif x < target:
                left += 1
                
            else:
                return [left+1,right+1]
            
            
        
        