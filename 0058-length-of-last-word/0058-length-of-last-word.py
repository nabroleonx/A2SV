class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        slow = -1
        while slow >= -n and s[slow] == ' ':
            slow-=1
        fast = slow
        while fast >= -n and s[fast] != ' ':
            fast-=1
        return slow - fast