# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_dist = float('inf')
        parent = float('-inf')
        
        def helper(node):
            nonlocal min_dist, parent
            if not node:
                return
            
            helper(node.left)
            
            min_dist = min(min_dist, node.val-parent)
            parent = node.val
            
            helper(node.right)
            
        helper(root)
        return min_dist