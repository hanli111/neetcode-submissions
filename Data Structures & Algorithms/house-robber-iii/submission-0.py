# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # returns a pair [with_root, without_root]
        def dfs(node):
            if not node:
                return [0, 0]
            
            left_pair = dfs(node.left)
            right_pair = dfs(node.right)

            with_root = node.val + left_pair[1] + right_pair[1]
            without_root = max(left_pair) + max(right_pair)

            return [with_root, without_root]
        
        return max(dfs(root))