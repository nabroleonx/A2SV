#Problem: https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        words = {}
        for i in s.split():
            words[i[-1]] = i[:-1]
        sorted_sentence = []
        for index, word in sorted(words.items()):
            sorted_sentence.append(word)
        return ' '.join(sorted_sentence) 
