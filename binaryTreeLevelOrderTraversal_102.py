# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #       call bfs() to scan the tree level by level and append each level in ans []
        return self.bfs(root)

    def bfs(self, root):
        ans = []
        if root:
            temp = []
            q = collections.deque()
            q.append(root)

            while q:
                length = len(q)
                while length > 0:
                    node = q.popleft()
                    temp.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    length -= 1
                ans.append(temp)
                temp = []

        return ans
