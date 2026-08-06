class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            stk = [(x, y)]
            curr_area = 0
            while stk:
                i, j = stk.pop()
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                    grid[i][j] = 0
                    curr_area += 1
                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nx, ny = i + dx, j + dy
                        stk.append((nx, ny))
            return curr_area

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res
