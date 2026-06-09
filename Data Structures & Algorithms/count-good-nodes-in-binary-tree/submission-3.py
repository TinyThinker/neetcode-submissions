# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, localMax):
            # Base case (end of traversal)
            if not root:
                return 0

            count = 0
            if localMax <= root.val:
                count += 1

            count += dfs(root.left, max(localMax, root.val))
            count += dfs(root.right, max(localMax, root.val))
            return count

        
        return dfs(root, float("-inf"))
        