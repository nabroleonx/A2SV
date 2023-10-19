class Trie():
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()
        
        for word in words:
            cur = root
            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = Trie()
                
                cur = cur.children[letter]
            
            cur.isEnd = True
            
        
        res = ""
        
        for word in words:
            if len(word) < len(res):
                continue
            
            cur = root
            for letter in word:
                cur = cur.children[letter]
                
                if not cur.isEnd:
                    break
            
            if cur.isEnd and (len(word) > len(res) or (len(word) == len(res) and word < res)):
                res = word        
            
        return res
            
            
            
                
        