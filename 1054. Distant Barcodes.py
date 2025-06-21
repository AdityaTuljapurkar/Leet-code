from typing import List
import heapq
from collections import Counter 
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter  = Counter(barcodes)
        maxheap = [[-cnt , val] for val ,cnt in counter.items() ] 
        heapq.heapify(maxheap)
        
        prev = None 
        res = []
        while maxheap : 
            #no prev 
            cnt , val = heapq.heappop(maxheap)
            res.append(val) 
            cnt +=1 

            if prev : 
                heapq.heappush(maxheap,prev)
                prev = 0 
            if cnt != 0 : 
                prev = [cnt , val ]
        
        return res
                
if __name__ == "__main__":
    sol = Solution()
    # Test case 1: Example from LeetCode
    barcodes = [1,1,1,2,2,2]
    result = sol.rearrangeBarcodes(barcodes)
    print("Test 1:", result)
            # Should not have two adjacent same numbers

            