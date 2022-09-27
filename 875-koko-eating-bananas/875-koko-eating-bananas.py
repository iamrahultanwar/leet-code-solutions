class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left,right = 1,max(piles)
        
        while left < right:
            
            speed = (left + right) // 2
            
            
            hourSpent = 0
            
            for pile in piles:
                hourSpent += math.ceil(pile/speed)
                
            
            if hourSpent <= h:
                right = speed
            else:
                left = speed + 1
                
                
        return right 