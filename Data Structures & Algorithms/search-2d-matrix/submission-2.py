class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1
        while L <= R:
            M = L + ((R - L) // 2)
            if target < matrix[M][0]:
                R = M - 1
            elif target > matrix[M][-1]:
                L = M + 1
            else:
                break
        
        # perform binary search on specific row to check for target
        l, r = 0, len(matrix[0]) - 1
        M = L + ((R - L) // 2)
        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[M][m] == target:
                return True
            elif matrix[M][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False


        '''
        find row where target lies within with BS
        then perform BS on that specific row to see
        if the target is actually in that row or not

        l   m       r
        0   1   2   3
        1   2   4   8       0 L
        10  11  12  13      1 M
        14  20  30  40      2 R
        '''