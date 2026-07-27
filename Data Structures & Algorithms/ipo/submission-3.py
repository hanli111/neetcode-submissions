class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # store (capital, profit)
        min_heap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_heap)
        max_heap = []
        
        for _ in range(k):
            while min_heap and w >= min_heap[0][0]:
                c, p = heapq.heappop(min_heap)
                heapq.heappush_max(max_heap, p)
            
            if not max_heap:
                break
            
            w += heapq.heappop_max(max_heap)
        return w