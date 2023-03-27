# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        
        def inorder(rootHead):
            if rootHead != None:
                inorder(rootHead.left)
                arr.append(rootHead.val)
                inorder(rootHead.right)
        
        inorder(root)
        
        return arr

        