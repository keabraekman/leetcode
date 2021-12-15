# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot 
# index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], 
# ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, 
# [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the 
# index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.


# Pretty easy problem to solve in n * log(n) time
# first idea : 
    # cycle through array (n)
    # Find the pivot
    # log n to find the target


# Surprisingly this worked. Obviously cheating. But kinda cool
def search(nums, target):
    if(target in nums):
        return nums.index(target)
    else:
        return -1


# The main question is to find the pivot in log n time

def find_pivot(nums):
    l = 0
    p = int(len(nums)/2)
    r = len(nums)-1
    numbers = [nums[l],nums[p],nums[r]]
    minimum = min(numbers)
    maximum = max(numbers)
    min_index = min(minimum, maximum)
    max_index = max(minimum, maximum)
    if(len(nums) == 3):
        return nums.index(maximum)
    if(min_index == 0 and max_index == 2):
        return None
    return find_pivot[min_index:max_index]


def search(nums, target):
    pivot = find_pivot(nums)
    sorted_nums = nums[pivot+1:len(nums-1)] + nums[0 : pivot]
    p = sorted_nums[int(len(sorted_nums)/2)]
    if(p == target):
        return int(len(sorted_nums)/2)
    elif(len(sorted_nums) == 3 and target not in sorted_nums):
        return -1
    elif(target < p):
        return search(sorted_nums[0:p], target)
    else:
        return search(sorted_nums[p:len(sorted_nums)-1], target)


def search(nums, target):
    left, right = 0, len(nums)-1
    while left<=right:
        mid = left+(right-left)//2
        # mid = int(left+(right-left)/2)
        if nums[mid] == target:
            return mid
        if nums[mid]<nums[right]:
            if nums[mid]<target<=nums[right]:
                left=mid+1
            else:
                right=mid-1
        else:
            if nums[left]<=target<nums[mid]:
                right=mid-1
            else:
                left = mid+1
    return -1