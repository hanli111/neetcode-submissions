class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            # base cases
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0: return 1
            if (r, c) in visited: return 0

            visited.add((r, c))
            perimeter = dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            return perimeter
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)
        return 0