# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        pairs = []
        
        while head:
            pairs.append(head.val)
            head = head.next
            
        max_sum = 0
        
        l, r = 0, len(pairs)-1
        
        while l<r:
            max_sum = max(max_sum, pairs[l]+pairs[r])
            
            l += 1
            r -= 1
        
        return max_sum