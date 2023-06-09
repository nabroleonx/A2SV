class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        
        words_sorted = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        res = [word[0] for word in words_sorted[:k]]

        return res
