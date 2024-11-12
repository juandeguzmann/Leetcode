def maxProfit(prices):
    maxProfit = 0
    left = 0
    right = 1

    while right < len(prices):
        if prices[right] < prices[left]:
            left = right
            right += 1
        else:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
            right += 1
    return maxProfit

prices = [10,1,5,6,7,1]

print(maxProfit(prices))