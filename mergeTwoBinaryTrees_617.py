"""
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


#         def merge(root1,root2):
#             if not root2:
#                 return
#             if not root1:
#                 root1 = root2
#             else:
#                 root1.val += root2.val

# #           to create a null child node
#             if not root1.left and root2.left:
#                 root1.left = TreeNode()
#             if not root1.right and root2.right:
#                 root1.right = TreeNode()

#             merge(root1.left,root2.left)
#             merge(root1.right,root2.right)

#         merge(root1,root2)

#         return root1 #root1 beacause we have merged the 2 trees in root1
