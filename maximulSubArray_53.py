"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""


def maxSubArray(nums):
    maxsum = nums[0]
    currsum = 0
    #         If the currsum becomes negative then simply discart the current subarray
    for i in nums:
        if currsum < 0:
            currsum = 0
        currsum += i
        maxsum = max(maxsum, currsum)  # To preserve sum of max sub Array
    return maxsum


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
