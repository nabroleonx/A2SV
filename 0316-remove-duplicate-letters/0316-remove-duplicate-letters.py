class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = {}
        visited = set()
        stack = []
        
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        
        for char in s:
            if char not in visited:
                while stack and freq[stack[-1]] > 0 and char < stack[-1]:
                    temp = stack.pop()
                    visited.remove(temp)
                stack.append(char)
                visited.add(char)
            freq[char] -= 1
        
        return ''.join(stack)
        