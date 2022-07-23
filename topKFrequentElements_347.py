import heapq
from collections import Counter, deque


class Solution:
    def add(self, val):
        if not self.ans or len(self.ans) < self.k:
            heapq.heappush(self.ans, val)
        elif self.ans[0][0] <= val[0]:
            heapq.heappushpop(self.ans, val)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #         Time O(k+NlogN)
        #         Space O(N+k)
        self.k = k
        self.ans = []
        count = Counter(nums)
        q = deque()
        for n, c in count.items():
            self.add((c, n))
        while k > 0:
            q.append(heapq.heappop(self.ans)[1])
            k -= 1
        return q
