# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashMap = defaultdict(list)
        
        def dfs(node, r, c):
            if not node:
                return
            hashMap[c].append((r, node.val))
            dfs(node.left, r+1, c-1)
            dfs(node.right, r+1, c+1)
            
            
        dfs(root, 0, 0)
        res = []
        col_sorted = sorted(hashMap.keys())
        
        for col in col_sorted:
            hashMap[col].sort()
            res.append([v for _, v in hashMap[col]])
        
        return res
            