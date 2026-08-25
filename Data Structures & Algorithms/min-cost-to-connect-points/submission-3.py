class DSU:
    def __init__(self, n):
        self.parent = list(range(n)) # or [i for i in range(n)]
        self.size = [1] * n

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        PRIM'S ALGORITHM
        '''
        # heap = [(0, 0)] # (dist, node index)
        # visited = set()
        # n = len(points)
        # res = 0
        # while len(visited) < n:
        #     dist, i = heapq.heappop(heap)
        #     if i in visited: continue
        #     res += dist
        #     visited.add(i)

        #     xi, yi = points[i]
        #     for j in range(n):
        #         if j not in visited:
        #             xj, yj = points[j]
        #             dist = abs(xi - xj) + abs(yi - yj)
        #             heapq.heappush(heap, (dist, j))
        # return res

        '''
        KRUSKAL'S ALGORITHM (DSU)
        '''
        edges = [] # (dist, x, y)
        n = len(points)
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                edges.append((dist, i, j))
        
        # must sort distance from least to greatest
        edges.sort()
        dsu = DSU(n)
        res = 0
        for dist, x, y in edges:
            if dsu.union(x, y):
                res += dist
        return res