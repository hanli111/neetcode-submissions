class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # ROWS, COLS = len(grid), len(grid[0])
        # visited = set()

        # def dfs(r, c):
        #     # base cases
        #     if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0: return 1
        #     if (r, c) in visited: return 0

        #     visited.add((r, c))
        #     perimeter = dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        #     return perimeter
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 1:
        #             return dfs(r, c)

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            perimeter = 0

            while q:
                r, c = q.popleft()

                # traverse 4 directions
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                        perimeter += 1
                    elif (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return perimeter
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return bfs(r, c)

