class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (board[r][c] == "."):
                    continue
                elif (board[r][c] in row_set[r] or board[r][c] in col_set[c] or board[r][c] in box_set[(r // 3, c // 3)]):
                    return False
                else:
                    row_set[r].add(board[r][c])
                    col_set[c].add(board[r][c])
                    box_set[(r // 3, c // 3)].add(board[r][c])
        return True
            