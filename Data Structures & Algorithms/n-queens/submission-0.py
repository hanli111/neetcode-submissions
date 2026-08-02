class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # pos_diag = r + c, neg_diag = r - c
        cols, pos_diag, neg_diag = set(), set(), set()
        res = []
        board = [["."] * n for i in range(n)]
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # update sets and board and recurse
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)

                # update sets and board for next recursive call
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return res