class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create a list of pair having position and speed
        pair = [[p,s] for p,s in zip(position,speed)]
        
        # sort the pair
        pair = sorted(pair)
        
        
        # reverse the pair
        
        pair = reversed(pair)
        
        stack = []
        
        for p,s in pair:
            stack.append((target - p) / s)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
                
        return len(stack)
            