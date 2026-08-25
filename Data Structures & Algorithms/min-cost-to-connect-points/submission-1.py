class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        PRIM'S ALGORITHM
        '''
        heap = [(0, 0)] # (dist, node index)
        visited = set()
        n = len(points)
        res = 0
        while len(visited) < n:
            dist, i = heapq.heappop(heap)
            if i in visited: continue
            res += dist
            visited.add(i)

            xi, yi = points[i]
            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]
                    dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(heap, (dist, j))
        return res