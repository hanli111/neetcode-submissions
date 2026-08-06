import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we want a max heap
        for i in range(len(stones)):
            stones[i] = -stones[i]

        max_heap = stones
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            val1 = -heapq.heappop(max_heap)
            val2 = -heapq.heappop(max_heap)

            if val1 > val2:
                heapq.heappush(max_heap, -(val1 - val2))

        max_heap.append(0)
        return abs(max_heap[0])
