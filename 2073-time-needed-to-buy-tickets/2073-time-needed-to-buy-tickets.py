class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        
        while tickets[k] != 0:
            for t in range(len(tickets)):
                if tickets[k] == 0:
                    break
                if tickets[t] == 0:
                    continue
                else:
                    tickets[t] -= 1
                    res += 1
        return res
            