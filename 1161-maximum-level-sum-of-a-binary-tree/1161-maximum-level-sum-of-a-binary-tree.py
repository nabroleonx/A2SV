# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        queue = deque()
        queue.append(root)
        level = 0
        depth = 0
        while queue:
            cur_sum = 0
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_sum += node.val
            
            depth += 1
            if cur_sum > max_sum:
                max_sum = cur_sum
                level = depth
        
        return level
                
                
        
        