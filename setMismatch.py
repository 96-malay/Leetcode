def findErrorNums( nums):
        nums = sorted(nums)
        for j in range(len(nums)):
            if(nums[j] != j+1):
                return [nums[j],j+1]


print(findErrorNums([3,2,3,4,6,5]))