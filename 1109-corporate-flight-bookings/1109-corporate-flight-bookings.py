class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*(n+1)
        for first, last, seats in bookings:
            res[first-1] += seats
            res[last] -= seats

        for i in range(1, len(res)):
            res[i] += res[i-1]
        
        res.pop()

        return res