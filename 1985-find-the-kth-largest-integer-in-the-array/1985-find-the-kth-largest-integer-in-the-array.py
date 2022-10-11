class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        sortedArr = [-int(i) for i in nums]
        heapq.heapify(sortedArr)
        
        while k > 1:
            heapq.heappop(sortedArr)
            k-=1
        return str(-sortedArr[0])
            