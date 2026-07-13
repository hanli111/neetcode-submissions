"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            all_same = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        all_same = False
                        break
            
            # if entire grid is the same, it's a leaf node and set value to grid[r][c] and all 4 children to null and return
            if all_same:
                return Node(val=grid[r][c], isLeaf=True, topLeft=None,
                            topRight=None, bottomLeft=None, bottomRight=None)
            
            # otherwise, recursively call dfs on the TL, TR, BL, and BR grids
            n = n // 2
            TL = dfs(n, r, c)
            TR = dfs(n, r, c + n)
            BL = dfs(n, r + n, c)
            BR = dfs(n, r + n, c + n)
            return Node(val=0, isLeaf=False, topLeft=TL,
                        topRight=TR, bottomLeft=BL, bottomRight=BR)
        
        # call dfs
        return dfs(len(grid), 0, 0)