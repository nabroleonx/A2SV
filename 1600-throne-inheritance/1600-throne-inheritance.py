class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.dead = set()
        self.children = defaultdict(list)

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)
    
    def successor(self, x, curOrder):
        if x not in self.dead:
            curOrder.append(x)
        
        for child in self.children[x]:
            self.successor(child, curOrder)

    def getInheritanceOrder(self) -> List[str]:
        curOrder = []
        self.successor(self.king, curOrder)
        return curOrder
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()