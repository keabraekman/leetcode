# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


def canJump(nums):
    goal = len(nums)-1
    for i in range(1,len(nums)):
        index = len(nums)-1-i
        if index + nums[index] >= goal:
            goal = index
    if goal == 0:
        return True
    else:
        return False

nums = [3,3,3,3,4]
print(canJump(nums))