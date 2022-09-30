#Problem: https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        array = []
        for i in nums1:
            length = len(array)
            k = nums2.index(i)
            for j in nums2[k:]:
                if j > i:
                    array.append(j)
                    break

            if len(array) == length:
                array.append(-1)

        return array
      
