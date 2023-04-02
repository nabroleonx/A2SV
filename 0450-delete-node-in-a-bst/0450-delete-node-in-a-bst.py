# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: 
            return
        else:
            if root.val < key: 
                root.right = self.deleteNode(root.right, key)
            elif root.val == key: 
                if not root.left or not root.right: 
                    return root.left or root.right 
                node = root.right 
                while node.left: 
                    node = node.left 
                root.val = node.val 
                root.right = self.deleteNode(root.right, node.val)
            else: 
                root.left = self.deleteNode(root.left, key)
        return root 