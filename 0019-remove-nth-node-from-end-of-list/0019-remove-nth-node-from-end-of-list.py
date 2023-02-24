# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        m = 0 # len of the linked list
        while cur != None:
            cur = cur.next
            m += 1
        
        if m == n : 
            return head.next
        
        cur = head
        
        for i in range(1,m-n):
            cur = cur.next
        cur.next = cur.next.next
        return head