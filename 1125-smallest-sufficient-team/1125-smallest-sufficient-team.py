class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        res = [''] * 17
        
        def dfs(x, has, path):
            nonlocal res
            if x == n:
                res = path
            elif req_skills[x] in has:
                dfs(x + 1, has, path)
            else:
                if len(path) + 1 < len(res):
                    for i, p in enumerate(people):
                        p = set(p)
                        if req_skills[x] in p:
                            union = p & has
                            has |= p
                            dfs(x + 1, has, path + [i])
                            has -= p
                            has |= union
                            
        dfs(0, set(), [])
        
        return res