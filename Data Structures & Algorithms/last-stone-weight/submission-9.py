class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:        
        max_heap = stones

        while len(max_heap) > 1:
            heapq.heapify_max(max_heap)
            s1 = heapq.heappop_max(max_heap)
            s2 = heapq.heappop_max(max_heap)

            diff = abs(s1 - s2)

            if s1 != s2:
                heapq.heappush_max(max_heap, diff)
            if not stones:
                return diff
            if len(stones) == 1:
                return stones[0]

        return(max_heap[0])