from typing import List , Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists :
            return None
        return self.splitList(lists , 0 ,len(lists)-1)
    
    def splitList(self, lists ,left ,  right ):
        if left ==  right : 
            return lists[left]
        mid =  (left+right)//2 
        left_split = self.splitList(lists ,left , mid)
        right_split = self.splitList(lists , mid+1 , right)
        return self.mergeList( left_split , right_split)
    
    def mergeList(self , left , right):
        dummy = ListNode()
        tail = dummy 

        while left and right :
            if left.val < right.val : 
                tail.next = left
                left = left.next 
            
            else : 
                tail.next = right  
                right = right.next    
            tail = tail.next
             
        tail.next = left if left else right 
        return dummy.next 