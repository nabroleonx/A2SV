class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = 0
        n = len(isConnected)

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1:
                    if j not in visited:
                        visited.add(j)
                        dfs(j)

        for i in range(n):
            if i not in visited:
                provinces += 1
                dfs(i)

        return provinces