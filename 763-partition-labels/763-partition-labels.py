class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # prepare a hashmap to store last index for every character
        
        lastIndex = {}
        
        for i,v in enumerate(s):
            lastIndex[v] = i
            
            
            
        result = [] # store result
        end,size = 0,0
        
        
        for i,v in enumerate(s):
            size += 1
            end = max(end,lastIndex[v])
            
            if i == end:
                result.append(size)
                size = 0
                
                
        return result
            