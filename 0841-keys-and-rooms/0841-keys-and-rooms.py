class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque()
        for i in rooms[0]:
            queue.append(i)
        
        locked = [True]*len(rooms)
        locked[0] = False
        
        while queue:
            cur = queue.popleft()
            locked[cur] = False
            visited.add(cur)
            for i in rooms[cur]:
                if i not in visited:
                    queue.append(i)
        
        for i in locked:
            if i:
                return False
        
        return True   
            