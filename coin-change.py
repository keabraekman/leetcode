# You are given an integer array coins representing coins of different 
# denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If 
# that amount of money cannot be made up by any combination of the coins, return 
# -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:

# Input: coins = [2], amount = 3
# Output: -1

# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

def coinChange(coins, amount):
    dp = [0] + [amount+1]*(amount)
    for a in range(1,amount+1):
        for c in coins:
            if a-c >= 0:
                dp[amount] = min(dp[a], 1 + dp[a-c])
    if dp[amount] < amount+1:
        return dp[amount]
    else:
        return -1








def coinChange(coins, amount):
    dp = [amount+1]*(amount+1)
    dp[0] = 0
    for a in range(1,amount+1):
        for c in coins:
            if a-c >= 0:
                dp[a] = min(dp[a], 1+dp[a-c])
    if dp[a] < amount+1:
        return dp[a]
    else:
        return -1


def coinChange(coins, amount):
    dp = [amount+1]*(amount+1)
    dp = 0
    for a in range(1,amount):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a-c]+1, dp[a])
    if dp[amount] < amount+1:
        return dp[amount]
    else:
        return -1