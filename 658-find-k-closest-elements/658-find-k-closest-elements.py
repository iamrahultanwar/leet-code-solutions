class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        sortedArr = sorted(arr,key=lambda num: abs(x-num))
        
        result = []
        
        
        for i in range(k):
            result.append(sortedArr[i])
            
        
        return sorted(result)