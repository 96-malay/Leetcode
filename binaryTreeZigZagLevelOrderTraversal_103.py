# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res, rev, q = [], True, deque()
        q.append(root)

        while q:
            length = len(q)
            temp, rev = [], not rev
            for _ in range(length):
                n = q.popleft()
                temp.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            if rev:
                res.append(reversed(temp))
            else:
                res.append(temp)
        return res
