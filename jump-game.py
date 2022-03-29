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











def canJump(nums):
    dp = [False]*(len(nums)-1)+[True]
    for i in range(len(nums)-2, -1, -1):
        for j in range(i, i+nums[i]):
            if j< len(nums) and dp[j]:
                dp[i] = True
    return dp[0]









nums = [3,3,3,3,4]
nums = [2,3,1,1,4]
print(canJump(nums))