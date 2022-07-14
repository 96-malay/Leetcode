# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = collections.deque()
        if root:
            q = collections.deque()
            q.append(root)
            while q:
                temp = []
                length = len(q)
                while length > 0:
                    node = q.popleft()
                    temp.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    length -= 1
                # Appending in reverse order.
                ans.appendleft(temp)
        return ans
