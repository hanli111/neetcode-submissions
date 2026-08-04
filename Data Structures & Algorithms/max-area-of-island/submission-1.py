class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c))
            cur_area = 1
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                cur_area += dfs(r + dr, c + dc)
            return cur_area
        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area