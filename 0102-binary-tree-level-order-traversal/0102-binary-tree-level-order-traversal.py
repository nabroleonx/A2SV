# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        level = 0
        queue = deque([root])
        
        while queue:
            temp = []
            for i in range(len(queue)):
                cur = queue.popleft()
                if not cur:
                    continue
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                    
                temp.append(cur.val)
            if temp:
                levels.append(temp)
        
        return levels
        