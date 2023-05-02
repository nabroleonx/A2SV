class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        h = len(haystack)
        n = len(needle)
        
        while n <= len(haystack):
            if haystack[index:n] == needle:
                return index
            else:
                index+=1
                n+=1
        return -1