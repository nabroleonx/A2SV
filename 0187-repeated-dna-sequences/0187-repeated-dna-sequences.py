class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashMap = {}
        res = []
        
        for i in range(len(s) - 9):
            key = s[i:i + 10]
            if key in hashMap:
                hashMap[key] += 1
                if hashMap[key] == 2:
                    res.append(key)
            else:
                hashMap[key] = 1
        return res