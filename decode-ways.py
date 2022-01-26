# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"

# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

#     "AAJF" with the grouping (1 1 10 6)
#     "KJF" with the grouping (11 10 6)

# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The test cases are generated so that the answer fits in a 32-bit integer.


def numDecodings(s):
    # Initiate dictionary. It's where we will store the number of decodings depending on i
    dp = {}
    # Initiate it with this value. If we reach the last digit, we only have one way to decode it
    dp[len(s)] = 1
    def dfs(i):
        # If we have already solved the problem, return the answer stored in the dict
        if i in dp:
            return dp[i]
        # If the current character is zero, return 0
        if s[i] == '0':
            return 0
        # the result is what is stored in the dictionary dp
        res = dfs(i+1)
        # If we have at least two characters left, and the two characters are smaller than 27
        if i < len(s)-1 and int(s[i] + s[i+1]) < 27:
            res += dfs(i+2)
        # store the result
        dp[i] = res   
        # return the result
        return res
    return dfs(0)




























def numDecodings(s):
    dp = {len(s) : 1}
    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == '0':
            return 0
        res = dfs(i+1)
        if i < len(s)-1 and int(s[i]+s[i+1])<27:
            res += dfs(i+2)
        return res
    return dfs(0)


s = "226"

print(numDecodings(s))
