class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        q = deque()
        total = 0
        
        
        while maxHeap or q:
            total += 1
            
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # pop the max value and sub one value as one task is processed

                if cnt:
                    q.append([cnt,total+n]) # add waiting time to the queue
                    
                    
            if q and q[0][1] == total: # check if we have the waiting time is over, add task back to maxheap
                heapq.heappush(maxHeap,q.popleft()[0])
                
                
        return total
                