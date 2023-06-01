class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        queue.append(['0000', 0])
        visited = set(deadends)
        
        if '0000' in visited:
            return -1
        
        def possibilities(code):
            res = []
            for i in range(4):
                turned = str((int(code[i]) + 1) % 10)
                res.append(code[:i]+turned+code[i+1:])
            
                turned = str((int(code[i]) - 1 + 10) % 10)
                res.append(code[:i]+turned+code[i+1:])
            return res
        
        while queue:
            code, move = queue.popleft()
            
            if code == target:
                    return move
                
            for i in possibilities(code):                
                if i not in visited:
                    visited.add(i)
                    queue.append([i, move+1])
                
        return -1