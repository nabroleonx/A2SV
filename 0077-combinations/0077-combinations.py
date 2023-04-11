class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def comb(i, n, k, cur_comb, all_combs):
            if len(cur_comb) == k:
                all_combs.append(cur_comb[:])
                return
            for j in range(i, n+1):
                cur_comb.append(j)
                comb(j+1, n, k, cur_comb, all_combs)
                cur_comb.pop()
        all_combs = []
        cur_comb = []
        comb(1, n, k, cur_comb, all_combs)
        return all_combs

