import heapq
import math 
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        #adding the number the left heap 
        heapq.heappush(self.left, -1*num)
        #if the left heap is larger than the right heap

        if(self.left and self.right and (-1*self.left[0]) > self.right[0] ):

            val = heapq.heappop(self.left)
            heapq.heappush(self.right,-1*val)

        #now checking for the size case  
        if len(self.left)> len(self.right)+1 :
            val = -1*heapq.heappop(self.left)
            heapq.heappush(self.right,val)
        if len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left,-1*val)
        

    def findMedian(self) -> float:
        #for odd number of elements
        if len(self.left) > len(self.right):
            return -self.left[0]
        if len(self.right) > len(self.left):
            return self.right[0] 
        #for even number of elements
        return (-self.left[0]+self.right[0])/2 
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()  
# obj.addNum(num)
# param num: int
# param: float
# median = obj.findMedian()

# Example usage:
obj = MedianFinder()
obj.addNum(-4)
print(obj.findMedian())  # Output: -4.0
obj.addNum(2) 
print(obj.findMedian())  # Output: 1.5
obj.addNum(3)
print(obj.findMedian())  # Output: 2.0
