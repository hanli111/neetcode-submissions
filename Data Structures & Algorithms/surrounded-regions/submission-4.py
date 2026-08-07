from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # if not board or not board[0]:
        #     return board

        m, n = len(board), len(board[0])
        q = deque()
        visited = set()

        # get left and right columns
        for r in range(m):
            if board[r][0] == "O" and (r, 0) not in visited:
                q.append((r, 0))
                visited.add((r, 0))
            if board[r][n-1] == "O" and (r, n-1) not in visited:
                q.append((r, n-1))
                visited.add((r, n-1))
        
        # get the top and bottom rows
        for c in range(n):
            if board[0][c] == "O" and (0, c) not in visited:
                q.append((0, c))
                visited.add((0, c))
            if board[m-1][c] == "O" and (m-1, c) not in visited:
                q.append((m-1, c))
                visited.add((m-1, c))

        # bfs
        while q:
            i, j = q.popleft()

            # check neighbors
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == "O" and (ni, nj) not in visited:
                    q.append((ni, nj))
                    visited.add((ni, nj))
        
        # loop through the board
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"

