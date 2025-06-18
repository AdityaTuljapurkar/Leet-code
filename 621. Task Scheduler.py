from typing import List
from collections import Counter  , deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) 
        heap = []
        time = 0
        q = deque()
        print (count)
        for key, value in count.items():
            heapq.heappush(heap, (-value))
        print ("the heap is :" ,heap)
        
        while heap or q:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time
    










tasks = ["A","A","A","B","B","B"]
n = 2
sol = Solution()
print(sol.leastInterval(tasks,n))