import heapq


class Solution:
    def add(self, val):
        if not self.ans or len(self.ans) < self.k:
            heapq.heappush(self.ans, val)
        else:
            if -val < -self.ans[0]:
                heapq.heappushpop(self.ans, val)

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Time: O(m*n)
        # Space: O(k)
        self.ans = []  # Max Heap
        self.k = k
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.add(-matrix[i][j])
        return -self.ans[0]
