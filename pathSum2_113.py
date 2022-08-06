# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, currsum, tmpres):
            if node is None:
                return
            currsum += node.val
            tmpres.append(node.val)
            if not node.left and not node.right:
                print(tmpres)
                if currsum == targetSum:
                    res.append(tmpres)
                tmpres.pop()
                # tmpres = []
                return
            dfs(node.left, currsum, tmpres)
            dfs(node.right, currsum, tmpres)
            return res
        dfs(root, 0, [])
        return res
