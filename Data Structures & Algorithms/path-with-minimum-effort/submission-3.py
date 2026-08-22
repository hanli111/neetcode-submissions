class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)] # or list(range(n))
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
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        '''
        # DIJKSTRA'S ALGORITHM
        ROWS, COLS = len(heights), len(heights[0])
        min_heap = [[0, 0, 0]] # [diff, row, col]
        visited = set()
        while min_heap:
            diff, r, c = heapq.heappop(min_heap)
            if (r, c) in visited: continue
            visited.add((r, c))
            if (r, c) == (ROWS - 1, COLS - 1): return diff

            # go through every neighbor
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited:
                    continue
                new_diff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(min_heap, [new_diff , nr, nc])
        return 0
        '''

        # KRUSKAL'S ALGORITHM
        ROWS, COLS = len(heights), len(heights[0])
        N = ROWS * COLS
        src, dst = 0, N - 1
        edges = [] # (weight, u, v), where u and v are the cell IDs it connects
        for r in range(ROWS):
            for c in range(COLS):
                cell_idx = r * COLS + c
                if r + 1 < ROWS:
                    edges.append([abs(heights[r][c] - heights[r + 1][c]), cell_idx, cell_idx + COLS])
                if c + 1 < COLS:
                    edges.append([abs(heights[r][c] - heights[r][c + 1]), cell_idx, cell_idx + 1])
        
        # must sort weight from increasing order
        edges.sort()
        dsu = DSU(N)
        for weight, u, v in edges:
            # once we union and the union has the source and destination, return the weight
            if dsu.union(u, v) and dsu.find(src) == dsu.find(dst):
                return weight
        return 0
