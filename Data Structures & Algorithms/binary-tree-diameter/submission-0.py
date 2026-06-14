# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            nonlocal max_dia
            l = dfs(node.left)
            r = dfs(node.right)
            max_dia = max(max_dia , l + r)
            return 1 + max(l , r)
        
        max_dia = 0
        dfs(root)
        return max_dia