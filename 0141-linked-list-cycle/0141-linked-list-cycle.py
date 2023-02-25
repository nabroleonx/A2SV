# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev = head
        hashMap = set()
        found = False
        while prev != None:
            hashMap.add(prev)
            if prev.next in hashMap:
                found = True
                break
            prev = prev.next   
        return found
    