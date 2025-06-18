from typing import List  
import heapq 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums ]
        heapq.heapify(maxHeap)

        for _ in range(k):
            kthLargest = -heapq.heappop(maxHeap)
        return kthLargest

# Example usage:
nums = [3, 2, 1, 5, 6, 4]
k = 2
sol = Solution()
print(sol.findKthLargest(nums, k))  # Output: 5