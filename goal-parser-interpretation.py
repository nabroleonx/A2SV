# Problem: https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        res = ''

        for i in range(len(command)):
            if command[i] == 'G':
                res += 'G'
            elif command[i] == '(':
                if command[i+1] == ')':
                    res += 'o'
                    i += 1
                else:
                    res += 'al'
                    i += 3
        return res
