class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumHash = {}
        
        for i,num in enumerate(nums):
            x = target - num
            if x in sumHash:
                return [sumHash[x],i]
            sumHash[num] = i
            