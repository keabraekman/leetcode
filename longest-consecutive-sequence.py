# Given an unsortedA array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    nums = list(set(nums))
    nums.sort()
    print('NUMS = ', nums)
    l, result, current = nums[0], 1, 1
    for i in range(1,len(nums)):
        if nums[i] == l + 1:
            current += 1
            result = max(result, current)
        else:
            current = 1
        l = nums[i]
    return result

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))

# We create an array the same length of tuples.
# Each element will be the number preceding the num and following number
# If there are no numbers, we remove the num from nums
# Then we start with the smallest number in nums, 
# Get the number following it
# Then we get the index of that number and start again

# NO. We sort the list. Way simpler.

