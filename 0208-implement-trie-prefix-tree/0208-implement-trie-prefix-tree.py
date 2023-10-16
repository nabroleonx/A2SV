class Trie:

    def __init__(self):
        self.isEnd = False
        self.children = [None]*26

    def insert(self, word: str) -> None:
        cur = self
        for letter in word:
            idx = ord(letter) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = Trie()
            cur = cur.children[idx]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.startsWith(word)
        return cur and cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for letter in prefix:
            idx = ord(letter) - ord('a')
            if not cur.children[idx]:
                return None
            cur = cur.children[idx]
        
        return cur


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)