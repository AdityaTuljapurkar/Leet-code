from typing import List
import heapq as h
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-val for val in stones]
        h.heapify(maxheap)
        while maxheap :
            if len(maxheap) > 1 :
                first = -h.heappop(maxheap)
                second = -h.heappop(maxheap)
                if first != second :
                    val = h.heappush(maxheap,-(first-second))
                if not maxheap and first == second :
                    return 0
            if len(maxheap) == 1 :break 
            
        return -maxheap[0]     
if __name__ == '__main__':
    stones = [2,7,4,1,8,1]
    print(Solution().lastStoneWeight(stones))
