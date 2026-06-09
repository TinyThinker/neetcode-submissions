# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.good_node_count = 0

    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, localMax):
            # Base case (end of traversal)
            if not root:
                return

            # Pre-order evaluation and traversal (root, left, right)
            if localMax <= root.val:
                self.good_node_count += 1

            dfs(root.left, max(localMax, root.val))
            dfs(root.right, max(localMax, root.val))

        dfs(root, float("-inf"))
        return self.good_node_count
        