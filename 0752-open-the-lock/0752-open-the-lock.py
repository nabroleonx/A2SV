class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque([('0000', 0)])
        visited = set(deadends)
        
        if '0000' in visited:
            return -1
        
        while queue:
            code, moves = queue.popleft()
            
            if code == target:
                return moves
            
            if code in visited:
                continue
            
            visited.add(code)
            
            for i in range(4):
                digit = int(code[i])
                for d in [-1, 1]:
                    turned = (digit + d) % 10
                    new_code = code[:i] + str(turned) + code[i+1:]
                    
                    if new_code not in visited:
                        queue.append((new_code, moves + 1))
        
        return -1

