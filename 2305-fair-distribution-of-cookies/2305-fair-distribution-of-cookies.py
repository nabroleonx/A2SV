class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        '''
            [6,1,3,2,2,4,1,2]


            cookies_sum = 21

            avg = cookies_sum // k

            avg = 7


            [8,15,10,20,8]

            sum = 61
            avg = 30

            34, 45, 31, 30 = 30

            - iterate over coolkies
            - add until you have sum >= avg
            - check the remaining and make sure remSum >= k * avg
            - if not, return false
        '''
        n = len(cookies)
        min_unfairness = float("inf")
        dist = [0 for _ in range(k)]
        
        def dfs(i):
            nonlocal dist, min_unfairness
            
            if i == n:
                min_unfairness = min(min_unfairness, max(dist))
                return
            
            if min_unfairness <= max(dist):
                return
            
            for j in range(k):
                dist[j] += cookies[i]              
                dfs(i+1)
                dist[j] -= cookies[i]
            
        dfs(0)

        return min_unfairness

            
            
        
    '''
        #         [8,15,10,20,8], A, 8, 10, 15, 20]
        # 
        #          [0, 0, 0, 0, 0]
        # total = 61, avg = 30
        # [8, 15, 10] = 33, total - 33 > avg, 61-33 = 28 < 30
        # [8, 15, 20] = 43, 61-43 = 18 < 30
        # [8, 15, 8]
        # 3-2 = 1 > 2'''
    
    