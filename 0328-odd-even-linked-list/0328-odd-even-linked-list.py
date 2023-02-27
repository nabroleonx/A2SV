# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = odd_head = ListNode(0)
        even = even_head = ListNode(0)
        i = 1
        while head != None:
            if i % 2 != 0:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            i += 1
        
        even.next = None
        odd.next = even_head.next
        
        return odd_head.next