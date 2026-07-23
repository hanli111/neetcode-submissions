class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for p in points:
            # x1 = 0, y1 = 0
            # x2 = p[0], y2 = p[1]
            dist = ((0 - p[0])**2 + (0 - p[1])**2) ** 0.5
            heapq.heappush(min_heap, (dist, p))
        
        res = []
        for _ in range(k):
            point = heapq.heappop(min_heap)
            res.append(point[1])
        return(res)