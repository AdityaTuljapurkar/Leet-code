from collections import deque 
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque()  # mono increasing
        max_q = deque()  # mono decreasing
        l = 0
        res = 0

        for r in range(len(nums)):
            while min_q and nums[r] < min_q[-1]:
                min_q.pop()
            while max_q and nums[r] > max_q[-1]:
                max_q.pop()
            
            max_q.append(nums[r])
            min_q.append(nums[r])
            
            # Move left pointer until the condition is valid
            while max_q[0] - min_q[0] > limit:
                if nums[l] == max_q[0]:
                    max_q.popleft()
                if nums[l] == min_q[0]:
                    min_q.popleft()
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
