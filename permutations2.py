# Given a collection of numbers, nums, 
# that might contain duplicates, return 
# all possible unique permutations in any order.


# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

def permuteUnique(nums):
    def backTracking(result, tempArray, nums, target):
        if len(target) == 0:
            if tempArray not in result:
                result.append(tempArray[:])
            tempArray = []
        else:
            for i in range(len(nums)):
                if(nums[i] in target):
                    tempArray.append(nums[i])
                    target.remove(nums[i])
                    backTracking(result, tempArray, nums, target)
                    tempArray.pop()
                    target.append(nums[i])

    result = []
    target = nums[:]
    backTracking(result, [], nums, target)
    return result



nums = [2,2,3,3,3]
print(permuteUnique(nums))