class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
            n = len(locations)
            dp = [[-1] * (fuel + 1) for _ in range(n)]
            def dfs(start, fuel):
                if dp[start][fuel] > -1:
                    return dp[start][fuel]
                cnt = 0
                if start == finish:
                    if fuel == 0:
                        return 1
                    elif fuel > 0:
                        cnt += 1
                for next in range(n):
                    if next == start:
                        continue
                    consume = abs(locations[next] - locations[start])
                    if consume > fuel:
                        continue
                    cnt += dfs(next, fuel - consume)
                dp[start][fuel] = cnt
                return dp[start][fuel]
            return dfs(start, fuel) % int(10 ** 9 + 7)