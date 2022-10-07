#Problem: https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0, len(height)-1
        max_area = 0
        while left < right:
            cont_area = (right-left) * min(height[left], height[right])
            if cont_area > max_area:
                max_area = cont_area
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_area
            class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0, len(height)-1
        max_area = 0
        while left < right:
            cont_area = (right-left) * min(height[left], height[right])
            if cont_area > max_area:
                max_area = cont_area
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_area
        
