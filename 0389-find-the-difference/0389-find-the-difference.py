class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashMap = {}
        for i in s:
            hashMap[i] = hashMap.get(i, 0) + 1
            
        for i in t:
            if i in hashMap:
                hashMap[i] -= 1
                if hashMap[i] == 0:
                    del hashMap[i]
            else:
                return i
        