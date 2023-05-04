class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = defaultdict(lambda: -1)
        stack = []
        
        for i in nums2:
            while stack and stack[-1] < i:
                next_greater[stack[-1]] = i
                stack.pop()
            stack.append(i)
            
        return [next_greater[i] for i in nums1]
                