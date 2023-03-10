class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        valid_op = '+-*/'
        for i in tokens:
            if i not in valid_op:
                stack.append(int(i))
            else:
                x = stack.pop()
                y = stack.pop()
                if i == "+":
                    stack.append(x+y)
                elif i == "-":
                    stack.append(y-x)
                elif i == "*":
                    stack.append(x*y)
                else:
                    stack.append(int(y/x))
        return stack[0]
    