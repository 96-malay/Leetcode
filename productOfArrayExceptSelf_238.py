class Solution:
    def productExceptSelf(self, nums):

        ans = []
        prefix = [1] * len(nums)
        post = [1]*len(nums)

        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(len(nums)-2, -1, -1):
            post[i] = post[i+1]*nums[i+1]
        for k in range(len(nums)):
            ans.append(prefix[k]*post[k])

        return ans
