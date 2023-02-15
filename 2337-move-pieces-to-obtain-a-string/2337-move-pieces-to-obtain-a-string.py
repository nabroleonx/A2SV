class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s, t = 0, 0
        
        if start.replace("_", "") != target.replace("_", ""):
            return False        
        
        while s < len(start) and t < len(start):
            while s < len(start) and  start[s] == "_":
                s += 1
            while t < len(start) and  target[t] == "_":
                t += 1
            
            if s < len(start) and t < len(start) and (start[s] == 'L' and s < t  or start[s] == 'R' and s > t):
                return False
        
            s += 1
            t += 1
        
        return True
    
        '''
        
        start  = "_L__R__R_" -> s
        target = "L______RR" -> t
        
        start =  "_L__R_L_R_"
        target = "L____RL__R"
        
        if start.replace("_", "") == target.replace("_", "")
        
        while start[s] == "_":
            s += 1
        while start[t] == "_":
            t += 1
        
        start[s] == 'L' and s > t  or start[s] == 'R' and s < t 
        
        s += 1
        t += 1


        -------s = 0, t = 0---------
        after the while s = 1, t = 0
        
        -------s = 1, t = 0---------      
        '''
        