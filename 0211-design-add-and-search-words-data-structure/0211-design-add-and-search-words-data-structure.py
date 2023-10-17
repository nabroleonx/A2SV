class WordDictionary:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def addWord(self, word: str) -> None:
        cur = self
        
        for c in word:
            idx = ord(c) - ord('a')
            if cur.children[idx] is None:
                cur.children[idx] = WordDictionary()
            cur = cur.children[idx]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(word, cur):
            for i in range(len(word)):
                c = word[i]
                idx = ord(c) - ord('a')
                if c != '.' and cur.children[idx] is None:
                    return False
                if c == '.':
                    for child in cur.children:
                        if child is not None and dfs(word[i + 1 :], child):
                            return True
                    return False
                cur = cur.children[idx]
            return cur.isEnd

        return dfs(word, self)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)