# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur != None:
            length += 1
            cur = cur.next
        
        mid = length//2
        cur = head
        for i in range(mid):
            cur = cur.next
        return cur