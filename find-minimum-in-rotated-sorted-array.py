# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

#     [4,5,6,7,0,1,2] if it was rotated 4 times.
#     [0,1,2,4,5,6,7] if it was rotated 7 times.

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

















def findMin(nums):
    if len(nums) >= 3:
        l, m, r = nums[0], nums[int(len(nums)/2)], nums[-1]
        if min(l, m, r) == l or (min(l,m,r) == m and nums[int(len(nums)/2)-1] < m):
            return findMin(nums[:int(len(nums)/2)])
        elif min(l,m,r) == r or (min(l,m,r) == m and nums[int(len(nums)/2)-1] > m):
            return findMin(nums[int(len(nums)/2):])
    else:
        return min(nums)
            

nums = [3,4,5,1,2]
# print(findMin(nums))































# Return wherever there is the largest difference

def findMin(nums):

    def recursion(nums):
        if len(nums) < 3:
            return min(nums)
        l,m,r = 0, int(len(nums)/2), len(nums)-1
        if nums[l] < nums[m] and nums[m] < nums[r]:
            return nums[l]
        elif abs(nums[l]-nums[m]) > abs(nums[m]-nums[r]):
            return recursion(nums[:m+1])
        else:
            return recursion(nums[m:])
    return recursion(nums)








def findMin(nums):
    l,m,r = 0,(len(nums)-1)//2, len(nums)-1
    while r > l+2:
        if max(nums[l], nums[m], nums[r]) == nums[m]:
            l = m
        elif min(nums[l], nums[m], nums[r]) == nums[m]:
            r = m
        else:
            r = m
        m = (r+l)//2
    return min(nums[l], nums[m], nums[r])




nums = [11,13,15,17]
print(findMin(nums))







