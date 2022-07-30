class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # Sliding Window. Some edge cases fail with this method
        l, r = 0, 0
        count = 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= k:
                if total == k:
                    count += 1
                total -= nums[l]
                l += 1
        return count
