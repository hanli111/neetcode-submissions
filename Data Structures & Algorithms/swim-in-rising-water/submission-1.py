class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # DIJKSTRA'S ALGORITHM
        heap = [(grid[0][0], 0, 0)] # (time, r, c)
        visited = set([0, 0])
        n = len(grid)
        while heap:
            time, r, c = heapq.heappop(heap)
            if (r, c) == (n - 1, n - 1): return time
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= n or (nr, nc) in visited: continue
                visited.add((nr, nc))
                heapq.heappush(heap, (max(time, grid[nr][nc]), nr, nc))