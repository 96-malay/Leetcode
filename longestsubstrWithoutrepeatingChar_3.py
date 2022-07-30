def lengthOfLongestSubstring(self, s: str) -> int:
    # Time: O(N)
    # Space: O(N)
    l, count, res = 0, {}, 0
    for r in range(len(s)):
        if s[r] in count:
            l = count[s[r]]+1
        res = max(res, r-l+1)
        count[s[r]] = r

    return res
