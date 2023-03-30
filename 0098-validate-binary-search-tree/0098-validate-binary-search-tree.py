# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        sorted_nodes = []
        
        def inorder(root, sorted_nodes):
            if not root:
                return
            inorder(root.left, sorted_nodes)
            sorted_nodes.append(root.val)
            inorder(root.right, sorted_nodes)
        
        inorder(root, sorted_nodes)
        
        for i in range(len(sorted_nodes)-1):
            if sorted_nodes[i] >= sorted_nodes[i+1]:
                return False
            
        return True