# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        prev = prev_head = ListNode()
        after = after_head = ListNode()
        
        while head:
            if head.val < x:
                prev.next = head
                prev = prev.next
            else:
                after.next = head
                after = after.next
            
            head = head.next
        
        after.next = None
        prev.next = after_head.next
        
        return prev_head.next
        