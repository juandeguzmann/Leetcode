def topKFrequent(nums, k):
    nums = sorted(nums)
    dictNum = {}
    results = []

    for i in range(len(nums)):
        if nums[i] in dictNum:
            dictNum[nums[i]] += 1
        else:
            dictNum[nums[i]] = 1

    for i in range(len(dictNum)):
        key = list(dictNum.keys())[i]
        results.append([key, dictNum[key]])
    
    results = sorted(results, key=lambda x: x[1], reverse=True)

    top_k = [results[i][0] for i in range(k)]

    return top_k



nums = [1,2,2,2,3,3,3]
k = 2

print(topKFrequent(nums, k))