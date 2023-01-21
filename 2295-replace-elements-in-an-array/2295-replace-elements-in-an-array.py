class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashMap = {value:index for index, value in enumerate(nums)}
        
        for x, y in operations:
            nums[hashMap[x]] = y
            hashMap[y] = hashMap[x]
            del hashMap[x]
        
        return nums