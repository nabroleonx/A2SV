# Problem: https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        characters = []
        pairs = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            if i in pairs.keys():
                characters.append(i)
            else:
                if len(characters) != 0 and characters[-1] not in pairs.values() and pairs[characters[-1]] == i:
                    characters.pop()
                else:
                    characters.append(i)


        return True if (len(characters) == 0) else False
