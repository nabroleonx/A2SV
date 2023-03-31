class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(nums,target):
            low = 0
            high = len(nums)-1

            while(low <= high):
                mid = (low+high)//2
                if nums[mid] == target and (target > nums[mid-1] or mid == 0):
                    return mid
                elif nums[mid] < target:
                    low = mid+1
                else:
                    high = mid-1
            return -1 
        
                        
        def last(nums,target):
            low = 0
            high = len(nums)-1

            while(low <= high):
                mid = (low+high)//2

                if ((nums[mid] == target) and (mid == len(nums)-1 or nums[mid+1] > target)):
                    return mid
                elif nums[mid] > target:
                    high = mid-1
                else:
                    low = mid + 1

            return -1
        
        return [first(nums, target), last(nums, target)]
