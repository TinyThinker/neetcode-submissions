# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # For this problem we can use DFS (depth first traversal).
        # We will use recursion for this.
        # Base condition will be when we have reached the end of 
        # a tree branch.

        # For each node, we will reverse the self.left and self.right

        if not root:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root      

        