# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = None

        def dfs(root):
            nonlocal count, res
            
            if not root:
                return

            dfs(root.left)
            if not count:
                return

            count -= 1
            if count == 0:
                res = root.val

            if not count:
                return
            dfs(root.right)

        dfs(root)
        return res