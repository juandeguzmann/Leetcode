trades = [(1, 100), (2, 110), (5, 90), (6, 120), (8, 105)]

def largestPriceChange(trades, windowSize):
    left = 0
    right = windowSize - 1
    maxPriceChange = 0

    while right <= len(trades) - 1:
        pricesInWindow = [trade[1] for trade in trades[left:right+1]]
        currentPriceChange = max(pricesInWindow) - min(pricesInWindow)
        maxPriceChange = max(maxPriceChange, currentPriceChange)
        right += 1
        left += 1
    return maxPriceChange

print(largestPriceChange(trades, 3))