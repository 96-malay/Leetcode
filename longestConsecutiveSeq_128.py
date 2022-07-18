import heapq


def longestConsecutive(nums):

    numSet = set(nums)
    longestSeq = 0

    for i in numSet:
        #           to start with smallest number in seq
        if i-1 not in numSet:
            currmax = 1
            currNum = i
            while currNum+1 in numSet:
                currNum += 1
                currmax += 1

            longestSeq = max(longestSeq, currmax)
    return longestSeq

# O(NlogN) time
# def longestConsecutive(nums):
#     if(len(nums) == 0):
#         return 0
#     nums = list(set(nums))
#     print(nums)
#     heapq.heapify(nums)
#     first = heapq.heappop(nums)
#     currMax = 1
#     res = 1
#     while nums:
#         num = heapq.heappop(nums)
#         if num == first + 1:
#             currMax += 1
#             first += 1
#         else:
#             first = num
#             currMax = 1
#         res = max(res, currMax)
#     return res
