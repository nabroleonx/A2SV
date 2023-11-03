class Solution:
    def decodeString(self, s: str) -> str:        
        stack = []

        for i in s:
            if i != ']':
                stack.append(i)
            else:
                temp = []
                while stack and stack[-1] != "[":
                    x = stack.pop()
                    temp.append(x)
                
                if stack[-1] == '[':
                    stack.pop()
                    
                    c = 0
                    i = 0
                    while stack and stack[-1] in '0123456789':
                        d = int(stack.pop())
                        c += d*10**i
                        i += 1

                    stack.append(''.join(reversed(temp))*c)

        return ''.join(stack)