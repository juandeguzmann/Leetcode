def longestConsecutive(nums):
    # Handle empty list case early
    if not nums:
        return 0

    # Sort the numbers to make consecutive sequence detection easier
    nums = sorted(nums)
    maxlcs = 1  # Maximum length of consecutive sequence found
    lcs = 1     # Current length of consecutive sequence

    # Iterate through the sorted list, starting from the second element
    for i in range(1, len(nums)):
        # Skip duplicates
        if nums[i] == nums[i - 1]:
            pass
        # Check if the current number is consecutive to the previous one
        elif nums[i] == nums[i - 1] + 1:
            lcs += 1
        else:
            # Reset current sequence length and update max length found
            maxlcs = max(maxlcs, lcs)
            lcs = 1  # Reset current sequence length for a new sequence

    # Return the maximum length found (checking one last time after the loop)
    return max(maxlcs, lcs)


nums1 = [2,20,4,10,3,4,5]
nums2 = [9,1,4,7,3,-1,0,5,8,-1,6]
print(longestConsecutive(nums2))

