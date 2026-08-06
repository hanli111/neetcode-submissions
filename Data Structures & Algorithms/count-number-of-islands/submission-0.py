class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        
        def dfs(x, y):
            stk = [(x, y)]

            while stk:
                x, y = stk.pop()

                if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                    grid[x][y] = "0"

                    for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
                        nx, ny = x + dx, y + dy
                        stk.append((nx, ny))
            
        res = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    res += 1
                    dfs(x, y)

        return res