class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #         Time : O(N)
        #         Space: O(1)
        l, r = 0, 0
        sumx = 0
        length = len(nums)+1
        while r < len(nums) and l < len(nums):
            sumx += nums[r]
            while sumx >= target:
                length = min(length, r-l+1)
                sumx -= nums[l]
                l += 1
            r += 1

        return 0 if length == len(nums)+1 else length


# #         Time : O(N^2)
# #         Space: O(1)
#         ans = inf

#         for i in range(len(nums)):
#             temp = 0
#             for j in range(i,len(nums)):
#                 temp += nums[j]
#                 if temp >= target:
#                     ans = min(ans,j-i+1)
#         return ans if ans != inf else 0
