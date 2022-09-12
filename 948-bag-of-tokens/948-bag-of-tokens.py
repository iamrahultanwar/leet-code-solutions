class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        
        q = deque(tokens)
        
        ans = bns = 0
        
        while q and (power >= q[0] or bns):
            while q and power >= q[0]:
                power -= q.popleft()
                bns += 1
                
            ans = max(ans,bns)
            
            if q and bns:
                power += q.pop()
                bns -= 1
                
        return ans
                
        