# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

def hammingWeight(n):
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res = res + bit
    return res


def hammingWeight(n):
    res = 0
    while n > 0:
        res += n%2
        n = n >> 1
    return res