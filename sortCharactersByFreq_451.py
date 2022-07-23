import heapq
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        #       Time O(N log N)
        #       Space O(N)
        maxHeap = []
        count = Counter(s)
        for char, freq in count.items():
            heapq.heappush(maxHeap, (-freq, char))
        ans = ''
        while maxHeap:
            obj = heapq.heappop(maxHeap)
            ans += obj[1] * -obj[0]
        return ans
