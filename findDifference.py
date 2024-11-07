def findDifference(nums1, nums2):
    dict1 = {}
    dict2 = {}
    result1 = []
    result2 = []

    for i, k in zip(nums1, nums2):
        if i in dict1:
            pass
        else:
            dict1[i] = i
        if k in dict2:
            pass
        else:
            dict2[k] = k
    
    for i in dict1:
        if i not in dict2:
            result1.append(i)
    
    for k in dict2:
        if k not in dict1:
            result2.append(k)
            
    
    print([result1, result2])


def findDifference(nums1, nums2):
    s1 = set(nums1)
    s2 = set(nums2)
    print([list(s1 - s2), list(s2 - s1)])

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

findDifference(nums1, nums2)