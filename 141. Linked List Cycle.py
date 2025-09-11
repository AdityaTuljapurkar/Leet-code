from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        val = set()
        while head : 
            if head not in val :
                val.add(head)
            elif head in val : 
                return True  
            head= head.next 
        
        return False 
    