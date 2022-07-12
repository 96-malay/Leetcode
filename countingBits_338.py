class Solution:
    def countBits(self, n):
        ans = [0]
        offset = 1

        for i in range(1, n+1):
            if i == offset*2:
                offset = i
            ans.append(1+ans[i-offset])
        return ans
