from typing import List
from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = [0]*len(deck)
        q = deque(range(len(deck)))
        for n in deck:
            i = q.popleft()
            res[i] = n 
            if q :
                q.append(q.popleft())
        return res
# Example usage:
sol = Solution()
print(sol.deckRevealedIncreasing([17,13,11,2,3,5,7]))
# Output: [2, 13, 3, 11, 5, 17, 7]
