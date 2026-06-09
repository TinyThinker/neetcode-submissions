# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # The BST properties of the tree informs that every for every node, 
        # the values on the left subtree as smaller and the values on the right subtree
        # are smaller than the value of the selected node.
        # This allows us to traverse the tree node by node and ask ourselves if this node is 
        # the LCA.
        # We will compare if the current node is larger or equal than the smaller node
        # and smaller or equal than the larger node. If this is true we know this is where 
        # we are branching creating a LCA
        # Fs the current node is larger than both nodes then we need to traverse the left tree and start again.
        # if the current node is smaller than both nodes then we need traverse the right side of the tree
        # we will process p and q to make p always the smaller and q the larger.
        if not root:
            return None

        if p.val > q.val:
            p, q = q, p

        if p.val <= root.val <= q.val:
            return root

        l = r = None
        if root.val < q.val:
           l = self.lowestCommonAncestor(root.right, p, q)
        else:
           r = self.lowestCommonAncestor(root.left, p, q)

        return l or r


