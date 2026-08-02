class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, pos_diag, neg_diag = set(), set(), set()
        res = 0
        #board = [["."] * n for i in range(n)]
        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return
            
            for c in range(n):
                if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                backtrack(r + 1)

                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
        backtrack(0)
        return res