from typing import List 
import heapq 
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        fuel = startFuel 
        i = 0 
        stop = 0 
        maxheap =  []
        while fuel <= target :
            while i < len(stations) and stations[i][0] <= fuel : 
                heapq.heappush(maxheap,-stations[i][1])
                i+=1 

            if not maxheap : 
                return -1 
            
            fuel += -heapq.heappop(maxheap)
            stop +=1 
        
        return stop 

if __name__ == '__main__' :
    print(Solution().minRefuelStops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))