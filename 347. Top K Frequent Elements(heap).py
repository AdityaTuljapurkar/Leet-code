from typing import List
from collections import Counter
import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for key, value in counter.items():
            if len(heap) < k :
                heapq.heappush(heap, (value, key))
            else:
                heapq.heappushpop(heap,(key,value))
                
        return [h[1] for h in heap ]
# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))  # Output: [1, 2]