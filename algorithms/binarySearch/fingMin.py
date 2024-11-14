def findMin(nums):
    leftIndex = 0
    rightIndex = len(nums)-1
    res = nums[0]

    while rightIndex >= leftIndex:
        if nums[leftIndex] < nums[rightIndex]:
            res = min(res, nums[leftIndex])
            break
        
        midIndex = (rightIndex + rightIndex) // 2
        res = min(res, nums[midIndex])
        if nums[midIndex] >= nums[leftIndex]:
            leftIndex = midIndex + 1
        else:
            rightIndex = midIndex - 1
    
    return res

nums = [1,2,3,4,5,6, 7]
print(findMin(nums))