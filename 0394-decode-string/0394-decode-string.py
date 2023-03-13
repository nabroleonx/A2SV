class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        n = 0
        stack = [""]
        
        while i < len(s):
            if s[i].isdigit():
                n = n * 10 + int(s[i])
            elif s[i] == "[":
                stack.append(n)
                n = 0
                stack.append("")
            elif s[i] == "]":
                es = stack.pop()
                rep = stack.pop()
                es2 = stack.pop()
                
                stack.append(es2 + es * rep)
            else:
                stack[-1] += s[i]
                
            i += 1           
        return "".join(stack)