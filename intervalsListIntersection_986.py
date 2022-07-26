class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):

            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans

# class Solution:
#     def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
#         if not firstList or not secondList:
#             return []
#         i,j = 0,0
#         f,s = firstList[i],secondList[j]
#         ans = []
#         while True:

#             if s[0] <= f[0] or s[1] >= f[0]:
#                 ans.append([max(s[0],f[0]),min(s[1],f[1])])
#                 i+=1

#             else:
#                 j+=1
#             if i < len(firstList) and j < len(secondList):
#                 f,s = firstList[i],secondList[j]
#             else:
#                 break
#         return ans
