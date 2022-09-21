# Product: https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_product = 1
        post_product = 1
        product_array = [1]

        for i in range(len(nums)-1):
            pref_product *= nums[i]
            product_array.append(pref_product)

        for i in range(len(nums)-1, -1, -1):
            product_array[i] *= post_product
            post_product *= nums[i]
        return product_array
                
