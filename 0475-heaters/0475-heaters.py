class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        heaters = [float('-inf')] + heaters + [float('inf')]

        min_radius = -1
        l = 0

        for house in houses:
            while heaters[l+1] < house:
                l += 1
            
            min_radius = max(min(heaters[l+1]-house, house-heaters[l]), min_radius)
        
        return min_radius