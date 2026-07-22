import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = sorted(nums, reverse=True)
        for i in range(len(self.max_heap)):
            self.max_heap[i] = -1 * self.max_heap[i]
        
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -1 * val)
        self.max_heap.sort()
        print(self.max_heap)
        return -1 * self.max_heap[self.k - 1]