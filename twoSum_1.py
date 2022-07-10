def twoSum(nums, target):
    dicto = {}
    for i in range(len(nums)):
        # Store each number with it's index in dict. search for 2nd number (target - current num) in dict.
        # Complexity: O(n)
        if target - nums[i] in dicto:
            return [dicto[target - nums[i]], i]
        else:
            dicto[nums[i]] = i
