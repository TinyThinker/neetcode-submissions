# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # We must find the height on each side of the three.
        # We can do a tree traversal and compute the max left and max right height
        # And comapre at the end.
        return self.dfs(root)[0]
        

    def dfs(self, root: TreeNode):
        if not root:
            return (True, 0)

        left, right = self.dfs(root.left), self.dfs(root.right)
        if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
            return (True, 1 + max(left[1], right[1]))
        else:
            return (False, None)

        




        



        

        
        