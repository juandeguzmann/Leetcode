def maxArea(nums):
    left = 0
    right = nums[-1]
    maxArea = 0

    for left in range(len(nums)):
        for right in range(left+1, len(nums)):
            currentArea = min(nums[left], nums[right]) * (right - left)
            maxArea = max(maxArea, currentArea)
    return maxArea

height = [1,7,2,5,4,7,3,6]
height = [2,2,2]
print(maxArea(height))


