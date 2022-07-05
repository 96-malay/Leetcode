"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
"""

# O(log n) Complexity


def findPeakElement(nums):
    # Binary search.
    l = 0
    r = len(nums)-1
    while(l <= r):
        if l == r:
            return l
        mid = (l+r) // 2
        if nums[mid] > nums[mid+1]:
            r = mid
        else:
            l = mid+1


print(findPeakElement([0, 1, 2, 3, 2, 1, 2, 6, 2, 1, 2, 4, 2, 1, 0]))
print(findPeakElement([1, 2, 3, 2, 1, 2, 6, 2, 1, 2, 4, 2, 1, 0]))
