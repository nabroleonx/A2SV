class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ch = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for i in s:
            if i in ch.values():
                stack.append(i)
            else:
                if stack != [] and stack[-1] == ch[i]:           
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0
    