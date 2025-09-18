from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dubSet = set()
        for num in nums :
            if num not in dubSet : 
                dubSet.add(num)
            elif num in dubSet :
                return num 
            