class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # pass one: find the row
        top, bot = 0, ROWS - 1
        while top <= bot:
            mid_row = (top + bot) // 2
            if target > matrix[mid_row][-1]:
                # check for bottom rows
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                # check for top rows
                bot = mid_row - 1
            else:
                # it's the current row
                break

        # check for invalid top and bot pointers
        if not (top <= bot):
            return False

        # pass two: find if target is in the row
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                # go right
                l = m + 1
            elif target < matrix[row][m]:
                # go left
                r = m - 1
            else:
                # found the target
                return True

        # target doesn't exist in matrix
        return False
