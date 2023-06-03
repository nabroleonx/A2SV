# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        def finder(node, d):
            if not node:
                return
            
            if d == 0:
                res.append(node.val)
            
            finder(node.left, d-1)
            finder(node.right, d-1)
            
                
            
        def dfs(node):
            if not node:
                return -1
            
            if node == target:
                finder(node, k)
                return 0
            
            left_dis, right_dis = dfs(node.left), dfs(node.right)
            
            d = max(left_dis, right_dis) + 1
            
            if left_dis == -1 and right_dis == -1:
                return -1
            
            opposite = node.left
            
            if k - d == 0:
                finder(node, 0)
            else:
                if left_dis != -1:
                    opposite = node.right
                
                finder(opposite, k-d-1)
            
            return d
            
        dfs(root)
        
        return res