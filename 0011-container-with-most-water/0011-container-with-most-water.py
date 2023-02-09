class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        most_water = -float("inf")
        
        while l < r:
            cur_area = min(height[l], height[r])*(r-l)
            
            most_water = max(most_water, cur_area)
            
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return most_water
            