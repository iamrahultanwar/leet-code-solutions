class HitCounter:

    def __init__(self):
        self.hits = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.hits[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        begin = timestamp - 300
        
        hitsForTs = 0
        
        
        for i in range(begin+1,timestamp+1):
            if i in self.hits:
                hitsForTs += self.hits[i]
                
        return hitsForTs


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)