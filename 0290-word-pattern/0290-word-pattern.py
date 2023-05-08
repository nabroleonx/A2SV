class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split(" ")
        
        if len(pattern) != len(s_arr):
            return False
        
        p_hash, s_hash = {}, {} 
        
        for ss, p in zip(s_arr, pattern): 
            if p in p_hash and p_hash[p] != ss: 
                    return False 
            p_hash[p] = ss 
            
            if ss in s_hash and s_hash[ss] != p: 
                    return False 
            s_hash[ss] = p
            
        return True