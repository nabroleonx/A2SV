class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverse(num):
            rev = 0
            while num > 0:
                rem = num%10
                rev = rev*10 + rem
                num = num//10
            return rev
        n = len(nums)
        for i in range(n):
            nums.append(reverse(nums[i]))
        return len(set(nums))
            