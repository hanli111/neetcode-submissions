class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
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
                if (nr < 0 or nr >= ROWS or nc < 0 
                    or nc >= COLS or (nr, nc) in visited): continue
                new_diff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(min_heap, [new_diff , nr, nc])
        return 0