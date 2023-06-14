# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        parent = float('-inf')
        min_diff = float('inf')
        
        def helper(node):
            nonlocal min_diff, parent
            if not node:
                return
            
            helper(node.left)
            
            min_diff = min(min_diff, abs(node.val - parent))
            parent = node.val
            
            helper(node.right)
        
        helper(root)
        
        return min_diff
            
        