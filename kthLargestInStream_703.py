import heapq


class KthLargest:
    stream = []

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        for i in range(len(nums)):
            self.add(nums[i])

    def add(self, val: int) -> int:

        if not self.stream or len(self.stream) <= self.k-1:
            heapq.heappush(self.stream, val)
        else:
            if val >= self.stream[0]:
                heapq.heappushpop(self.stream, val)

        return self.stream[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Test case:
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

# ["KthLargest","add","add","add","add","add"]
# [[1,[]],[-3],[-2],[-4],[0],[4]]
