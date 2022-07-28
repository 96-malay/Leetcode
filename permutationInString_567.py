class Solution:
    #     Time: O(n) - linear for window sliding and counter
    #     Space: O(1) - conctant for dictionary with the maximum 26 pairs (English alphabet)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #       get the freq of each letter in s1 in hashmap
        data = Counter(s1)
        b = len(s1)
        for i in range(len(s2)):
            if s2[i] in data:
                data[s2[i]] -= 1
            if i >= b and s2[i-b] in data:
                data[s2[i-b]] += 1
            # if freq of all the letters in hashmap is 0, it means s2 contains a permutation of s1
            if all([data[i] == 0 for i in data]):
                return True
        return False


#       TLE
        # comb = set()
        # i=0
        # s1length = len(s1)
        # while i<= len(s2) - s1length:
        #     comb.add(''.join(sorted(s2[i:i+s1length])))
        #     i+=1
        # # print(comb)
        # s1 = ''.join(sorted(s1))
        # return True if s1 in comb else False
