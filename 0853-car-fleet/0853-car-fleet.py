class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        tm = -1
        arr = list(zip(position, speed))
        arr.sort(reverse=True)
        
        for p, s in arr:
            time_left = (target-p)/s
            if time_left > tm:
                res += 1
                tm = time_left
        
        return res
        