from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count the frequency of each character in the string
        counter = Counter(s)
        # Build a max heap based on character frequency (negative for max heap)
        maxheap = [[-value, char] for char, value in counter.items()]
        heapq.heapify(maxheap)
        
        res = ''    # Result string
        prev = None # Store the previous character and its count if it still has remaining occurrences
        
        # Continue until there are no more characters to process
        while maxheap or prev:
            # If there's a leftover character but no other character to pair with, return ""
            if prev and not maxheap:
                return ''
            
            # Pop the character with the highest remaining count
            val, char = heapq.heappop(maxheap)
            res += char      # Add it to the result
            val += 1         # Decrease its count (since val is negative)
            
            # If there was a previous character waiting, push it back into the heap
            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            
            # If the current character still has remaining occurrences, save it for the next round
            if val != 0:
                prev = [val, char]
        
        return res

# Example usage:
sol = Solution()  
print(sol.reorganizeString("aab"))  # Output: "aba"