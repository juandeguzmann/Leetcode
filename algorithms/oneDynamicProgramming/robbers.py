def rob(nums):
    rob1, rob2 = 0, 0

    for num in nums:
        temp = max(num + rob1, rob2)
        print(temp)
        rob1 = rob2
        rob2 = temp
    return rob2

rob([1,1,3,3])