from typing import List
from collections import deque
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #using siliding window with heap
        # using mototnic queue with sliding window  
        res =  []
        stack = deque()
        #creating a user function for adding stuff 
        def Add(index:int ,  stack:deque):
            while stack and nums[stack[-1]] < nums[index] :
                stack.pop()
            stack.append(index)
            
        for i in range(k):
            Add(i,stack)
        
        res.append(nums[stack[0]])

        start = 0 
        end  = k-1 
        while end < len(nums)-1:
            # removing start  
            start +=1 
            if stack[0] <= start :
                stack.popleft()
            #adding end 
            end += 1 
            Add(end,stack)
            res.append(nums[stack[0]])

        return res 
    





            
            


            
        
    

print(Solution().maxSlidingWindow( [1,3,-1,-3,5,3,6,7], k = 3))