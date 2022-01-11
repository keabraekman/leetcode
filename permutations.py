# Given an array nums of distinct integers, 
# return all the possible permutations. You 
# can return the answer in any order.

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],
# [3,1,2],[3,2,1]]


def backTracking(result, tempArray, target, nums):
    # target = numbers we can still use
    if len(target) == 0:
        result.append(tempArray[:])
        target = nums
        tempArray = []
    else:
        for i in range(len(nums)):
            if(nums[i] in target):
                tempArray.append(nums[i])
                target.remove(nums[i])
                backTracking(result, tempArray, target, nums)
                tempArray.pop()
                target.append(nums[i])



def permute(nums):
    result = []
    backTracking(result, [], nums[:], nums)
    return result

print(permute([1,2,3]))