class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        
        s1_hashMap = {}
        for i in s1:
            s1_hashMap[i] = s1_hashMap.get(i, 0) + 1
        
        l, r = 0, n-1
        
        s2_hashMap = {}
        for i in s2[l:r+1]:
            s2_hashMap[i] = s2_hashMap.get(i, 0) + 1
        
        if s1_hashMap == s2_hashMap:
            return True
            
        while r < len(s2)-1:
            s2_hashMap[s2[l]] -= 1
            
            r += 1
            s2_hashMap[s2[r]] = s2_hashMap.get(s2[r], 0) + 1
            
            if s2_hashMap[s2[l]] == 0:
                del s2_hashMap[s2[l]]
                
            l += 1   
            if s1_hashMap == s2_hashMap:
                return True
        
        return False
    