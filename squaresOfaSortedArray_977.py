import collections


class Solution:
    #     -----Complexity O(nlogn)-----
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     for j in range(len(nums)):
    #         nums[j] = nums[j] * nums[j]
    #     # nums = nums.sort()
    #     # print(nums)
    #     return sorted(nums)

    #   -----Complexity O(n)-----
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        result = collections.deque()
        while l <= r:
            #   Since the numbers are sorted,
            #   we will compare the abs value of left and right numbers, square the larger number and add in queue in non decreasing order
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                result.appendleft(left*left)
                l += 1
            else:
                result.appendleft(right*right)
                r -= 1
        return result
