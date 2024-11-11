def bubbleSort(numbers):
    size = len(numbers)

    for k in range(size - 1):
        swapped = False

        for i in range(size - 1 - k):
            if numbers[i] > numbers[i+1]:
                highNumber = numbers[i]
                lowNumber = numbers[i + 1]
                numbers[i] = lowNumber
                numbers[i + 1] = highNumber
                swapped = True
            
        if not swapped:
            break
    print(numbers)
            
# numbers = [9, 7, 4, 5, 2, 8, 1, 6, 3]
# bubbleSort(numbers)


def bubbleSortDict(elements, key):
    size = len(elements)

    for k in range(size - 1):
        swapped = False

        for i in range(size - 1 - k):
            if elements[i][key] > elements[i+1][key]:
                highNumber = elements[i][key]
                lowNumber = elements[i+1][key]
                elements[i][key] = lowNumber
                elements[i+1][key] = highNumber
                swapped = True
            
        if not swapped:
            break
    print(elements)


elements = [
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]

bubbleSortDict(elements, key='name') 