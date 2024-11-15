def totalProfit(nums):
    left = 0
    right = 1
    total = 0

    while right <= len(nums) - 1:
        if nums[right] < nums[left]:
            left = right
            right += 1
        else:
            profit = nums[right] - nums[left]
            total += profit
            left = right
            right += 1
    return total

nums1 = [7, 1, 5, 3, 6, 4]
nums2 = [1, 2, 3, 4, 5]
nums3 = [7, 6, 4, 3, 1]

print(totalProfit(nums3))