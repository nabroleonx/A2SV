class MapSum:

    def __init__(self):
        self.hashMap = defaultdict(int)
        self.words = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        if key in self.words:
            self.words[key], val = val, val - self.words[key]
        else:
            self.words[key] = val
        
        for i in range(len(key)):
            prefix = key[:i+1]
            self.hashMap[prefix] += val

    def sum(self, prefix: str) -> int:
        return self.hashMap[prefix]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)