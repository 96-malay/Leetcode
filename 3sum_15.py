def threeSum(nums):
    nums.sort()
    res = []

    for i, a in enumerate(nums):

        if i > 0 and nums[i-1] == nums[i]:
            continue
        l = i+1
        r = len(nums)-1
        while l < r:
            target = a + nums[l]+nums[r]
            if target > 0:
                r -= 1
            elif target < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while(nums[l] == nums[l-1] and l < r):
                    l += 1
    return res
