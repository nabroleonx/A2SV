# Problem: https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum_array = []
        prefix_sum = 0
        for i in nums:
            prefix_sum += i
            self.prefix_sum_array.append(prefix_sum)

    def sumRange(self, left: int, right: int) -> int:
        if right > 0 and left > 0:
            return self.prefix_sum_array[right] - self.prefix_sum_array[left-1]
        else:
            return self.prefix_sum_array[right]
          
