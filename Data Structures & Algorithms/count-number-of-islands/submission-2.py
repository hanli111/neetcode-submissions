class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        DEPTH FIRST SEARCH
        '''
        # ROWS, COLS = len(grid), len(grid[0])
        # islands = 0
        # def dfs(r, c):
        #     if r < 0 or c < 0 or c >= COLS or r >= ROWS or grid[r][c] == "0":
        #         return
            
        #     grid[r][c] = "0"
        #     for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        #         dfs(r + dr, c + dc)
            
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == "1":
        #             dfs(r, c)
        #             islands += 1
        # return islands

        '''
        BREADTH FIRST SEARCH
        '''
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        def bfs(r, c):
            grid[r][c] = "0"
            q = deque([(r, c)])
            while q:
                r, c = q.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0":
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands