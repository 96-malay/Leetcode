"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

#Boyer-Moore Voting Algorithm O(n) Time and O(1) Space Complexity
"""
# class Solution:
#   Space Complexity O(n) because Sorted() creates a new list of size n
#   Time complexity O(nlogn)
#     def majorityElement(self, nums: List[int]) -> int:
#         return (sorted(nums)[floor(len(nums)/2)] if len(nums)>1 else nums[0])


class Solution:
    #   Space Complexity O(n)
    #   Time complexity O(n)
    def majorityElement(self, nums):
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for k, v in count.items():
            if v > len(nums) // 2:
                return k

# class Solution:
# #   Boyer-Moore Voting Algorithm
# #   Space Complexity O(1)
# #   Time complexity O(n)
#     def majorityElement(self, nums):
#         count = 0
#         candidate = None

#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += (1 if num == candidate else -1)

#         return candidate
