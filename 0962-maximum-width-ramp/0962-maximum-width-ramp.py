class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maxWidth = 0
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]: 
                stack.pop()
            stack.append(i)

        i = 0
        for j in range(len(nums)):
            while i < len(stack) and nums[stack[i]] >= nums[j]:
                maxWidth = max(maxWidth, stack[i] - j)
                i += 1

        return maxWidth