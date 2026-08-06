import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # helper function to find Euclidean distance
        def dist(x, y):
            return (math.sqrt((x**2) + (y**2)))

        max_heap = [] # (dist from origin, coordinate points)

        for point in points:
            max_heap.append((-dist(point[0], point[1]), point))

        # turns it into a max heap
        heapq.heapify(max_heap)

        # pop from the top while the length of the heap is greater than k
        while len(max_heap) > k:
            heapq.heappop(max_heap)

        # remaining elements are the k closest to origin
        res = []
        for i in range(len(max_heap)):
            res.append(max_heap[i][1])

        return res