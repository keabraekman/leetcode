numbs = [2,7,11,15]
target = 9
def twoSum(nums):
        for i in range(len(nums)):
            diff = target - nums[i]
            if((diff in nums) and (nums.index(diff) != i)):
                return [i, nums.index(diff)]