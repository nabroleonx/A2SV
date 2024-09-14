class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = Counter(s)
        for i in range(len(s)):
            if hash_map[s[i]] == 1:
                return i
        
        return -1