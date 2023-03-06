class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()     
        p, t = 0, 0
        count = 0
        i = 0
        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                p += 1
                t += 1
                count += 1
            else:
                t += 1
        return count
                