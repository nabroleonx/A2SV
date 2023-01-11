class Solution:
    def printVertically(self, s: str) -> List[str]:
        s_list = s.split(" ")
        maxL = len(max(s_list, key=len))
        ptr = 0
        res = []
        for i in range(maxL):
            v = []
            for word in s_list:
                if i < len(word):
                    v.append(word[i])
                else:
                    v.append(' ')
            res.append(''.join(v).rstrip())
        return res



