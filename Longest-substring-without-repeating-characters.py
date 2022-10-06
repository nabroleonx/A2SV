#Problem - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_arr = []
        left_ptr = 0
        max_len = float("-inf")
        
        for i in range(len(s)):
            while s[i] in curr_arr:
                curr_arr.remove(curr_arr[0])
                left_ptr += 1
            
            curr_arr.append(s[i])
            max_len = max(max_len, i-left_ptr+1)
            
        return 0 if max_len == float("-inf") else max_len
      
