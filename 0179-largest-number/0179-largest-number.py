class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        cur_max = ""
        res = ""
        while nums:
            for i in nums:
                if not cur_max:
                    cur_max=i
                else:
                    if i+cur_max > cur_max+i:
                        cur_max = i
            res+=cur_max
            nums.remove(cur_max)
            cur_max=""
        return str(int(res))
    