import heapq


class Solution:
    def add(self, val):
        if not self.minHeap or len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        elif self.minHeap[0] <= val:
            heapq.heappushpop(self.minHeap, val)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(N log N)
        # Space: O(N)
        self.minHeap = []
        self.k = k
        for n in nums:
            self.add(n)
        return self.minHeap[0]

        # Solution 2
        # return heapq.nlargest(k, nums)[-1]
