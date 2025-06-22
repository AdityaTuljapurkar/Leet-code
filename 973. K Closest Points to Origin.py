from typing import List 
import heapq 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#[[3,3],[5,-1],[-2,4]], k = 2
#(i.e., √(x1 - x2)2 + (y1 - y2)2).
        values = []
        result = []
        for arr in points :
            val =   (arr[0] ** 2 + arr[1] ** 2) ** 0.5
            appendval = []
            appendval.append(val)
            appendval.append(arr)
            values.append(appendval)

        heapq.heapify(values)
        i = 0
        print(values)
        while i < k :
            val = heapq.heappop(values)
            result.append(val[1])
            i +=1
        return result

    

print(Solution().kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))