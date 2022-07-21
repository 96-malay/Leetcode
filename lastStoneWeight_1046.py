import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ans = []
        for n in stones:
            heapq.heappush(ans, -n)  # Max Heap

        while len(ans) > 1:
            x = -heapq.heappop(ans)
            y = -heapq.heappop(ans)
            # if x == y then we do not need to add back anything else add back the remaining weight
            if x > y:
                heapq.heappush(ans, -(x-y))

        return -ans[0] if ans else 0
