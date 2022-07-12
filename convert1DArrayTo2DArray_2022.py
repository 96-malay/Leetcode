class Solution:
    def construct2DArray(self, original, m, n):
        if m*n != len(original):
            return []
        result = []
        temp = []
        nCopy = n
        for i in original:
            if nCopy > 0:
                temp.append(i)
                nCopy -= 1
            else:
                result.append(temp)
                nCopy = n
                temp = [i]
                nCopy -= 1

        if temp:
            result.append(temp)
        return result
