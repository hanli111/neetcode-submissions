class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv: return False
        if self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        return True

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        DISJOINT SET UNION
        '''
        ROWS, COLS = len(grid), len(grid[0])
        dsu = DSU(ROWS * COLS)

        # create index for each cell
        def index(r, c):
            return r * COLS + c
        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                            continue
                        dsu.union(index(r, c), index(nr, nc))
                    area = max(area, dsu.size[dsu.find(index(r, c))])
        return area


        # visited = set()
        # ROWS, COLS = len(grid), len(grid[0])
        # def dfs(r, c):
        #     if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visited:
        #         return 0
            
        #     visited.add((r, c))
        #     cur_area = 1
        #     for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #         cur_area += dfs(r + dr, c + dc)
        #     return cur_area
        
        # area = 0
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         area = max(area, dfs(r, c))
        # return area

