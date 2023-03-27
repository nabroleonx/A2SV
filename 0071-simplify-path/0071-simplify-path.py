class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        path = path.split("/")
        
        for i in path:
            if stack and i == "..":
                stack.pop()
            elif i != "" and i != "." and i != "..":
                stack.append(i)
                
        if stack == []:
            return "/"
            
        return "/"+'/'.join(stack)