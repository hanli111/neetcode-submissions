# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for i, val in enumerate(inorder):
            hashmap[val] = i
        
        self.curr_idx = 0
        def dfs(l, r):
            if l > r:
                return None
            root_val = preorder[self.curr_idx]
            self.curr_idx += 1
            root = TreeNode(root_val)
            R_idx = hashmap[root_val]
            root.left = dfs(l, R_idx - 1)
            root.right = dfs(R_idx + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)