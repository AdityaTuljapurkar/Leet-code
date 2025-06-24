from typing import List
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
       #using two heaps for the same 
       #heap1 to stope min - capitals
        #heap2 to store max profits 
        maxprofits = []
        mincapitals = [(c ,p) for c , p in zip(capital,profits)]
        heapq.heapify(mincapitals)
        print(mincapitals)
        
        for _ in range(k):
            while mincapitals and mincapitals[0][0]<=w :
                c,p = heapq.heappop(mincapitals)
                heapq.heappush(maxprofits,-p)
            if not maxprofits : break
            w += -heapq.heappop(maxprofits)
        return w
    
        



print(Solution().findMaximizedCapital( k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]))        