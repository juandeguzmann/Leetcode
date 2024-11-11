def longestSubarray(nums):
    numZeros = 1  # Allow one zero to be removed
    left = 0  # Left pointer for the sliding window
    maxN = 0  # Maximum length of subarray with at most one zero removed

    for right in range(len(nums)):
        if nums[right] == 0:
            numZeros -= 1  # Count the zero in the window

        # Shrink the window if we have more than one zero
        if numZeros < 0:
            if nums[left] == 0:
                numZeros += 1  # Move left pointer and restore numZeros if a zero is removed from the window
            left += 1  # Move left pointer

        # Update maxN with the current window size, subtracting one to simulate removing one zero
        maxN = max(maxN, right - left)

    return maxN

        




nums = [0,1,1,1,0,1,1,0,1]

print(longestSubarray(nums))