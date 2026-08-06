from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        q = deque()
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        num_fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == FRESH:
                    num_fresh += 1
                elif grid[i][j] == ROTTEN:
                    q.append((i, j))

        if num_fresh == 0:
            return 0
        
        num_mins = -1
        while q:
            num_mins += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == FRESH:
                        grid[nx][ny] = ROTTEN
                        num_fresh -= 1
                        q.append((nx, ny))
        
        return num_mins if num_fresh == 0 else -1