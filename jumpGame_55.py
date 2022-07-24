class Solution:

    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        ans = True
        i = len(nums)-2
        while i >= 0:
            if i + nums[i] >= target:
                ans = True
                target = i
            else:
                ans = False
            i -= 1
        return ans
