class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()        
        l, r = 0, len(skill)-1 
        summ = skill[0] + skill[-1]
        chemistry = 0
        while l<r:
            if skill[l] + skill[r] == summ:
                chemistry += (skill[l] * skill[r])
                r-=1
                l+=1
            else:
                return -1
        return chemistry
            