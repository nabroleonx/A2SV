class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.myheap = nums
        
        heapq.heapify(self.myheap)
        
        while len(self.myheap) > k:
            heapq.heappop(self.myheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.myheap, val)
        
        if len(self.myheap) > self.k:
            heapq.heappop(self.myheap)
        
        return self.myheap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)