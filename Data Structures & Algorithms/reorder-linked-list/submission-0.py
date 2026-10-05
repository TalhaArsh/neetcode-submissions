# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f = head, head.next

        while f and f.next:
            print(s.val, f.val)
            s = s.next
            f = f.next.next

        secondHalf = s.next
        s.next = None
        prev = None
        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf #final head is stored here 
            secondHalf = temp 
        
        first,second = head, prev

        while second :
            t1, t2 = first.next,second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2

        
            

        