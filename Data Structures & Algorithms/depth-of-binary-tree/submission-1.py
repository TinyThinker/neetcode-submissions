# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # We are going to use a DFS approach with recursion.
        # Identifying the base case.
        # If node is none then return. We have reached the last child on that branch.

        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left) + 1
        right = self.dfs(root.right) + 1

        return max(left, right)

        