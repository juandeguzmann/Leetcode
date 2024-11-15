def movingAverage(nums, windowSize):
    left = 0
    res = []

    while left <= len(nums) - windowSize:
        sumOfPriceInWindow = sum(nums[left: left + windowSize])
        movingAverageVal = sumOfPriceInWindow / windowSize
        res.append(movingAverageVal)
        left += 1

    return res