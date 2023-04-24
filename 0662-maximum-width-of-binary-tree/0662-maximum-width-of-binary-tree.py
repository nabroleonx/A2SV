# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1
        nodes = deque()
        nodes.append((root, 0))
        
        while nodes:
            indices = []
            for i in range(len(nodes)):
                node, idx = nodes.popleft()
                indices.append(idx)
                
                if node.left:
                    nodes.append((node.left, idx*2+1))
                if node.right:
                    nodes.append((node.right, idx*2+2))
                
            
            res = max(res, indices[-1]-indices[0]+1)
                
        return res
                
                
            
        
        
        
        
            
        '''
        actual_none = 0
        node_none = 0
        res = 0
        
        def helper(root):
            if not root.left and not root.right:
                return helper(root.left || root.right)
                 
        '''