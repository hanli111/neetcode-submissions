from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_q = deque()
        p_set = set()
        a_q = deque()
        a_set = set()

        m, n = len(heights), len(heights[0])

        # get all pacific ocean points
        for i in range(1, m):
            p_q.append((i, 0))
            p_set.add((i, 0))
        for j in range(n):
            p_q.append((0, j))
            p_set.add((0, j))

        # get all atlantic ocean points
        for i in range(m):
            a_q.append((i, n-1))
            a_set.add((i, n-1))
        for j in range(n-1):
            a_q.append((m-1, j))
            a_set.add((m-1, j))

        def bfs(q, seen):
            coords = set()
            while q:
                x, y = q.popleft()
                coords.add((x, y))
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        q.append((nx, ny))

        bfs(p_q, p_set)
        bfs(a_q, a_set)
        return list(p_set.intersection(a_set))



