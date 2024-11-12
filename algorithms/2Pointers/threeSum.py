def threeSum(nums):
    target = 0
    results = set()  # Use a set to store unique triplets
    nums = sorted(nums)  # Sort to manage duplicates
    
    for i in range(len(nums)):
        for k in range(i + 1, len(nums)):
            for j in range(k + 1, len(nums)):
                summation = nums[i] + nums[k] + nums[j]
                if summation == target:
                    # Add as tuple to the set to avoid duplicates
                    results.add((nums[i], nums[k], nums[j]))

    # Convert each tuple back to a list to match the desired output format
    return [list(triplet) for triplet in results]

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))