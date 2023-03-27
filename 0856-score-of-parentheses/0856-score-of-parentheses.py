class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        res = 0
        for i in s:
            if i == "(":
                stack.append(res)
                res = 0
            elif i == ")":
                if res:
                    res *= 2
                else:
                    res = 1
                res += stack.pop()  
        return res
    