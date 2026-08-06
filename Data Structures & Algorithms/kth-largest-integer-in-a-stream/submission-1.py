import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        # min heap
        min_heap = self.nums
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, val)

        # check if the size of the heap is greater than k
        while len(min_heap) > self.k:
            heapq.heappop(min_heap)
        
        return min_heap[0]

