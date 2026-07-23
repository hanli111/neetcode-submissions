class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = nums
        for i in range(len(max_heap)):
            max_heap[i] = -max_heap[i]
        heapq.heapify(max_heap)

        for _ in range(k - 1):
            heapq.heappop(max_heap)

        return -1 * max_heap[0]