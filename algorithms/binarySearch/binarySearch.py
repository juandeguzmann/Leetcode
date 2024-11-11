def binarySearch(numbers, target):
    numbers = sorted(numbers)
    rightIndex = len(numbers) - 1
    leftIndex = 0
    
    while leftIndex <= rightIndex:
        midNumberIndex = rightIndex - leftIndex // 2
        if numbers[midNumberIndex] == target:
            return midNumberIndex
        elif target > numbers[midNumberIndex]:
            leftIndex = midNumberIndex + 1
        else:
            rightIndex = midNumberIndex - 1
    return 'Not found'

def find_all_occurances(numbers, number_to_find):
    index = binarySearch(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)

if __name__ == '__main__':
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15
    indices = find_all_occurances(numbers, number_to_find)
    print(f"Indices of occurances of {number_to_find} are {indices}")
