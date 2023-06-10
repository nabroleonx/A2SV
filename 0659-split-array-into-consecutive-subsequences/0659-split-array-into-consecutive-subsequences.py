class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        subsequences = defaultdict(int)
        
        for num in nums:
            if freq[num] == 0:
                continue
            
            freq[num] -= 1
            
            if subsequences[num-1] != 0:
                subsequences[num-1] -= 1
                subsequences[num] += 1
            
            elif freq[num+1] > 0 and freq[num+2] > 0:
                subsequences[num+2] += 1
                freq[num+1] -= 1
                freq[num+2] -= 1
            
            else:
                return False
        
        return True
