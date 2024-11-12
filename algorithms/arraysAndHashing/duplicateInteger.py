def hasDuplicate(nums):
    dictNums = {}
    numberIndex = 0
    while numberIndex < len(nums):
        number = nums[numberIndex]
        if number in dictNums:
            numberIndex += 1
            return True
        else:
            dictNums[number] = number
            numberIndex += 1
    return False

nums = [1, 2, 3, 5, 1]
print(hasDuplicate(nums))