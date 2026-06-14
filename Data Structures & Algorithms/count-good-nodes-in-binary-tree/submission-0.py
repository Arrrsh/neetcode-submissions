# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, curr):
            nonlocal res
            if not node:
                return 
            if node.val >= curr.val:
                res += 1
                curr = node
            dfs(node.left, curr)
            dfs(node.right, curr)
        dfs(root, root)
        return res