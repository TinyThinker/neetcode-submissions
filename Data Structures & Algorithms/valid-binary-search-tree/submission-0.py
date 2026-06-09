# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # A valid tree:
        # left subtree of every node contains only nodes with values less than the node's value.
        # right subtree of every node contains only nodes with values greater thant the nodes value.
        # Both subtrees are binary search trees.
        # To be able to prove that a tree is valid bst we need to do it at a local and a global level.
        # We can achieve this simultaneously by having a boundary for the values of the node.
        # For example, the first node can be anything there are no boundaries. 
        #               we can express this in python with float("-inf") and float('inf')
        # We evaluate if the node is within the boundary.
        # If yes, we traverse the left and the right trees. But first we update the boundary.
        # If traversing the left subtree the new boundary is [low, node.val] since 
        # since we are moving to the left where nodes should be smaller we now that the new boundary
        # is that the high boundary is less than the previous node.
        # When traversing the right subtree we have the opposite [node.val, high] since we now that
        # the low boundary is a new one. The node cannot be smaller than the previous node.
        # As we keep updating this boundary, we make sure that the tree is not only locally
        # valid but it doesn't lose the bigger picture of what the previous nodes ahve done.
        # Corner cases. Are empty trees a BST? By definition yeah since no nodes violate the
        # BST property.
        return self.isValid(root, float("-inf"), float("inf"))

    def isValid(self, root, low, high):
        if not root:
            return True

        if not low < root.val < high:
            return False

        return self.isValid(root.left, low, root.val) and self.isValid(root.right, root.val, high)