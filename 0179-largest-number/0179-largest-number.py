class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        res = []
        while nums:
            cur_sum = ''
            for i in nums:
                if not cur_sum:
                    cur_sum = i
                else:
                    if i + cur_sum > cur_sum + i:
                        cur_sum = i
            res.append(cur_sum)
            nums.remove(cur_sum)
        
        return str(int(''.join(res)))