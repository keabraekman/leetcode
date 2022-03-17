# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] 
# is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10


def countBits(n):
    ans, offset = [0]*(n+1), 1
    for i in range(1,n+1):
        if offset*2 == i:
            offset *= 2
        ans[i] = 1 + ans[i-offset]
    return ans