# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        q = collections.deque()
        q.append(root)

#       Outer loop is for levels
        while q:
            l = len(q)
            sumt = 0
            # Inner loop computes the sum & Avg of nodes in each level
            for i in range(l):
                node = q.popleft()
                sumt += node.val
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)

            result.append(sumt/l)
        return result
