
def characterReplacement(s, k):
    # time: O(26N)
    # Space O(N)
    l, count = 0, {}
    res = 0  # Result substring length

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        while r-l+1 - max(count.values()) > k:  # validating current window
            count[s[l]] -= 1
            l += 1
        res = max(res, r-l+1)
    return res
