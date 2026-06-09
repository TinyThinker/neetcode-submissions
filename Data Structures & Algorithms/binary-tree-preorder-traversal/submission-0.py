# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        data = []
        def dfs(root, data):
            if not root:
                return

            data.append(root.val)
            dfs(root.left, data)
            dfs(root.right, data)

        dfs(root, data)
        return data