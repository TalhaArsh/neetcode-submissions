# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        headPtr = head
        r = ListNode()
        l = None

        slow = fast = head
        
        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            l = slow
            slow = slow.next
        if l is None:
            return head.next
        l.next = slow.next

        return headPtr

                
            
            

         
        
        