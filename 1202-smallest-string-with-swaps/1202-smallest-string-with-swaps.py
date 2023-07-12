class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))
        rank = [1]*n
        def find(node):
            if parent[node]!=node:
                parent[node] = find(parent[node])
            return parent[node]
        def union(i, j):
            root_i,root_j = find(i),find(j)

            if root_i == root_j:
                return
            
            if rank[root_i] > rank[root_j]:
                root_i, root_j = root_j, root_i

            parent[root_i] = root_j
            rank[root_j] += rank[root_i]

        for a, b in pairs:
            union(a, b)

        sets = defaultdict(list)
        
        for i in range(n):
            sets[find(i)].append(s[i])

        for set in sets.values():
            set.sort(reverse=True)
        
        res = []
        for i in range(n):
            res.append(sets[find(i)].pop())

        return ''.join(res)