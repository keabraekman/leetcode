# You are given an array prices where prices[i] is the price of a given stock on 
# the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and 
# choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot 
# achieve any profit, return 0.


# This is wrong. This is if you can do multiple trades. In this problem 
# we can only do one trade
def maxProfit(prices):
    result = 0
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            result += prices[i+1]-prices[i]
    return result




def maxProfit(prices):
    if len(prices) < 2:
        return 0
    l, r, result = 0, 1, max(0, prices[1] - prices[0])
    while r < len(prices):
        if prices[r] > prices[l]:
            result = max(result, prices[r] - prices[l], 0)
        else:
            l = r
        r += 1
    return result


prices = [7,1,5,3,6,4]
print(maxProfit(prices))