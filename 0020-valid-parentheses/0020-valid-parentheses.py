class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = '({['
        cl = ']})'
        
        ch = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for i in s:
            if i in op:
                stack.append(i)
            elif i in cl:
                if stack != [] and stack[-1] == ch[i]:           
                    stack.pop()
                else:
                    return False
            
        return True if len(stack) == 0 else False