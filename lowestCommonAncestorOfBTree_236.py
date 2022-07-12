# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Time Complexity O(2^H) H is height of tree
    # Space Complexity O(H) H is height of tree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return False
        if root.val == p.val or root.val == q.val:
            if self.lowestCommonAncestor(root.left, p, q) == True or self.lowestCommonAncestor(root.right, p, q) == True:
                return root
            else:
                return True
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            if left != False and right != False:
                return root
            else:
                return left or right
