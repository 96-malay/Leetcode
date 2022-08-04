# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Time: O(2N)
        # Space: O(N)
        if not root:
            return
        res, q = [], deque([root])

        while q:
            length = len(q)
            for _ in range(length):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            # n will always be the right most node of each level
            res.append(n.val)
        return res
