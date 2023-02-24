# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        left_head = dummy
        cur = head
        
        for i in range(left-1):
            left_head = cur
            cur = cur.next
            
        prev = None
        after = None
        for i in range(right-left+1):
            after = cur.next
            cur.next = prev
            prev = cur
            cur = after
        
        left_head.next.next= cur
        left_head.next = prev
        
        return dummy.next