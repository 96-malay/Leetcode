# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        # Backtracking
        res = []

        def backtracking(node, path):
            path.append(str(node.val))
            if not node.left and not node.right:
                ans = '->'.join(path)
                path.pop()
                res.append(ans)
                return

            if node.left:
                backtracking(node.left, path)  # path is passed by reference
            if node.right:
                backtracking(node.right, path)  # path is passed by reference
            path.pop()  # path is passed by reference, Hence we nned to pop last value
        backtracking(root, [])
        return res
