# Give you one sorted array, please put them into n buckets, we need to ensure we get n sub array with approximately equal weights.
# Example;
# input {1, 2, 3, 4, 5} n = 3
# output [[[5],[1,4],[2,3]];

def balancedSubsets(array,n):
    target = sum(array)/n
    
    return []