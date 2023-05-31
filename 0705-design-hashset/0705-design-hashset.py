class MyHashSet:

    def __init__(self):
        self.hash_set = [[] for _ in range(10000)]
        self.queries = 10000

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hash_set[key%self.queries].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hash_set[key%self.queries].remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.hash_set[key%self.queries]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)