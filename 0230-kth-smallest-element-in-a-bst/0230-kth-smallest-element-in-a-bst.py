# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        def inorder(root, k, nums):
            if not root:
                return
            inorder(root.left, k, nums)
            nums.append(root.val)
            inorder(root.right, k, nums)
        
        inorder(root, k, nums)
        return nums[k-1]
                