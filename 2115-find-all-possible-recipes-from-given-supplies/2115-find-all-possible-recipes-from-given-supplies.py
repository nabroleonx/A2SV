class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        adj = defaultdict(list)
        canMake = defaultdict(int)
        
        res = []
        
        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                adj[ingredient].append(recipes[i])
                indegree[recipes[i]] += 1
                canMake[recipes[i]] = 1
        
        queue = deque(supplies)
        
        while queue:
            supply = queue.popleft()
            if canMake[supply]:
                res.append(supply)
            
            for recipe in adj[supply]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    queue.append(recipe)
                    
        return res