# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        candidates = []
        self.search(root, subRoot, candidates)

        for root in candidates:
            if self.compare(root, subRoot):
                return True

        return False

    def compare(self, root, subroot):
        if not root and not subroot:
            return True

        if not root or not subroot or root.val != subroot.val:
            return False

        if self.compare(root.left, subroot.left) and self.compare(root.right, subroot.right):
            return True
        else:
            return False

        
        
    def search(self, root, subroot, l):
        if not root:
            return

        if root.val == subroot.val:
            l.append(root)

        self.search(root.left, subroot, l)
        self.search(root.right, subroot, l)
        

        

        
        