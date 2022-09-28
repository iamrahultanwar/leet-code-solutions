class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1

        
        left,right = 1,max(bloomDay)
        
        while left < right:
            
            mid = (left + right) // 2
            
            f = b = 0
            
            for day in bloomDay:
                f = 0 if day > mid else f + 1
                
                if f >= k:
                    f = 0
                    b += 1
                    
                    if b == m: break
                        
            if b == m:
                right = mid
            else:
                left = mid + 1
                    
                    
                    
        return left