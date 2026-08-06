# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        min_heap = []
        q = deque([root])

        while q:
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                heapq.heappush(min_heap, node.val)
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        #print(min_heap)
        for i in range(k-1):
            heapq.heappop(min_heap)
        
        #print(min_heap)
        return min_heap[0]