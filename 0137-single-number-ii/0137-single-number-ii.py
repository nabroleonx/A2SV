class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        appeared_once = 0
        appeared_twice = 0
        
        for num in nums:
            # print(f'num = {num}, -- once = {appeared_once}, twice= {appeared_twice} , not once= {~appeared_once} , not twice = {~appeared_twice} ')
            appeared_once = (appeared_once ^ num) & ~appeared_twice
            appeared_twice = (appeared_twice ^ num) & ~appeared_once
            
        return appeared_once