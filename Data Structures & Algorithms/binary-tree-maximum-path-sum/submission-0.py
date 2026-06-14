# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            nonlocal max_gain
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            max_gain = max(max_gain, node.val + left_max + right_max)
            return node.val + max(left_max, right_max)
        max_gain = float('-inf')
        dfs(root)
        return max_gain