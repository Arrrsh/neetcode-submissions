# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            nonlocal prev
            if prev >= node.val:
                return False
            prev = node.val
            return inorder(node.right)
        prev = float("-inf")
        return inorder(root)
