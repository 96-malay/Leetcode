# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxInd(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] >= nums[i]:
                i = j
        return i

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return
        part = self.maxInd(nums)  # Max num index
        root = TreeNode(nums[part])
        root.left = self.constructMaximumBinaryTree(nums[0:part])
        root.right = self.constructMaximumBinaryTree(nums[part+1:])
        return root
