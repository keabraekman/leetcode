# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

def maxSubArray(nums):
    l, r = 0, len(nums)-1
    curr = 0
    total = sum(nums[l:r+1])
    while curr < r:
        if total < sum(nums[curr:r+1]):
            total = sum(nums[curr:r+1])
            l = curr
        curr += 1
    curr = r
    total = sum(nums[l:r+1])
    while curr > l:
        if total < sum(nums[l:curr+1]):
            total = sum(nums[l:curr+1])
            r = curr
        curr -= 1
    print(l)
    print(r)
    if l + 1 == r :
        return max(nums[l], nums[r], sum(nums[l:r+1]))
    return sum(nums[l:r+1])


nums = [-1,-1,-2,-2]

print(maxSubArray(nums))