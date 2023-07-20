class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        stack = []
        
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] < abs(asteroid):
                    stack.pop()
                    
                if not stack:
                    res.append(asteroid)
                    
                else:
                    if stack[-1] == abs(asteroid):
                        stack.pop()
        res += stack
        
        return res