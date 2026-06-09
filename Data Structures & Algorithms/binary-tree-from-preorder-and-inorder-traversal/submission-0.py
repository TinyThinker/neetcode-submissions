# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {val:i for i, val in enumerate(inorder)} # this map will allow us to do fast efficient
                                                         # searches in the inorder array
        root_idx = 0
        def dfs(l, r):
            if l > r:
                return None

            # Get preorder root
            nonlocal root_idx
            root_val = preorder[root_idx]
            root = TreeNode(root_val)
            root_idx += 1

            mid = in_map[root_val]
            root.left = dfs(l, mid -1)
            root.right = dfs(mid + 1, r)

            return root

        low, high = 0, len(preorder) -1
        return dfs(low, high)

        



