# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        hashMap = set()
        found = False
        while prev != None:
            hashMap.add(prev)
            if prev.next in hashMap:
                found = True
                break
            prev = prev.next   
        
        if found:
            return prev.next
        else:
            return None
    