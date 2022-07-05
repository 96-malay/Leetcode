"""
Let's call an array arr a mountain if the following properties hold:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, 
return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
"""


def peakIndexInMountainArray(arr):

    for i in range(1, len(arr)-1):
        if arr[i] > arr[i+1]:  # Since the array is in increasing order, we only need to check for the point where values start decreasing
            return i


print(peakIndexInMountainArray([1, 2, 3, 2, 1]))
