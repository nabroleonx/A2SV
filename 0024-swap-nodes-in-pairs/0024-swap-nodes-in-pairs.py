# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = newH = ListNode()
        
        while head and head.next:
            nxt = head.next.next
            newH.next = head.next
            
            head.next.next = head
            newH = head
            head = nxt
            
        newH.next = head
        return dummy.next