import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #       Time: O(n + k log(n))
        dist = []
        for x, y in points:
            dist.append(((x**2+y**2)**0.5, [x, y]))

        heapq.heapify(dist)
        ans = []
        while k > 0:
            ans.append(heapq.heappop(dist)[1])
            k -= 1
        return ans
