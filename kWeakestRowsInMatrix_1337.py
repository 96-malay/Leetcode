import heapq


class Solution:
    # def add(self,val):
    #     if not self.strength or len(self.strength) < self.k:
    #         heapq.heappush(self.strength,val)
    #     else:
    #         if val[0] > self.strength[0][0]:
    #             heapq.heappushpop(self.strength, val)

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        self.strength = []
        self.k = k

        for i in range(len(mat)):
            j = 0
            count = 0
            while j < len(mat[i]) and mat[i][j] == 1:
                count += 1
                j += 1
            # self.add((-count,i))
            self.strength.append((count, i))
        res = []
        heapq.heapify(self.strength)  # minHeap
        print(self.strength)
        while k > 0:
            s, r = heapq.heappop(self.strength)
            res.append(r)
            k -= 1
        return res
