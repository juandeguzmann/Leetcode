def equalPairs(grid): #exceeds time complexity
    rowDict = {}
    columnDict = {}
    
    for k, row in zip(range(len(grid)), grid):
        rowDict[k] = row
    
    i = 0
    for col in zip(*grid):
        columnDict[i] = list(col)
        i += 1
    
    count = 0
    for x in rowDict:
        for y in columnDict:
            print(rowDict[x], columnDict[y])
            if rowDict[x] == columnDict[y]:
                count += 1
    
    print(count)

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
equalPairs(grid)