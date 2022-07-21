class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        dicto = {
            1: 'Gold Medal',
            2: 'Silver Medal',
            3: 'Bronze Medal'
        }
        sortedset = {}
        sortedlist = sorted(score, reverse=True)
        for i, v in enumerate(sortedlist):
            print(i, v)
            sortedset[v] = i+1
        ans = []
        for i in range(len(score)):
            if sortedset[score[i]] in dicto:
                ans.append(dicto[sortedset[score[i]]])
            else:
                ans.append(str(sortedset[score[i]]))
        return ans
