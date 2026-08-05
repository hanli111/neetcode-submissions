class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi-source BFS
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        # go through the grid and start at a treasure chest
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        def add_grid(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or grid[r][c] == -1:
                return
            q.append((r, c))
            visited.add((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    add_grid(r + dr, c + dc)
            dist += 1