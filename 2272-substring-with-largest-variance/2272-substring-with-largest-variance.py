class Solution:
    def largestVariance(self, s: str) -> int:
        max_variance = 0
        
        perm = permutations(set(s), 2)
        
        for char1, char2 in perm:
            count_char1 = 0
            has_char2 = False
            first_char2 = False
            
            for char in s:
                if char == char1:
                    count_char1 += 1
                
                if char == char2:
                    has_char2 = True
                    
                    if first_char2 and count_char1 >= 0:
                        first_char2 = False
                    else:
                        count_char1 -= 1
                        
                        if count_char1 < 0:
                            first_char2 = True
                            count_char1 = -1
                
                if has_char2 and count_char1 > max_variance:
                    max_variance = count_char1

        return max_variance