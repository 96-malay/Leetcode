# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time Complexity O(n) Space Complexity O(H)
    i = 0

    def bstFromPreorder(self, A, bound=float('inf')):
        if self.i == len(A) or A[self.i] > bound:
            return None
        root = TreeNode(val=A[self.i])
        self.i += 1
        root.left = self.bstFromPreorder(A, root.val)
        root.right = self.bstFromPreorder(A, bound)
        return root

    # Time Complexity O(n^2) Space Complexity O(H)
    # def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
    #     if not preorder:
    #         return None
    #     root = TreeNode(val=preorder[0])
    #     left = [x for x in preorder if x < root.val]
    #     right = [x for x in preorder if x > root.val]
    #     root.left = self.bstFromPreorder(left)
    #     root.right = self.bstFromPreorder(right)
    #     return root
