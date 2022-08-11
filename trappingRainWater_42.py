def trap(height):
    # Cal highest height in left side of curr point
    left = [0]
    lmax = height[0]
    for i in range(1, len(height)):
        lmax = max(height[i-1], lmax)
        left.append(lmax)

    # Iterate from right to left.
    # Amount of water that can be trapped at any point is min(leftHighest,rightHighest) - Current height
    ans = 0
    rmax = height[-1]  # this will indicate highest height from right side
    for i in range(len(height)-2, 0, -1):
        val = min(left[i], rmax) - height[i]
        ans += val if val > 0 else 0
        rmax = max(rmax, height[i])
    return ans
