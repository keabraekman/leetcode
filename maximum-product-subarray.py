# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.




def maxProduct(nums):

    def recursion(nums):
        print(nums)
        if len(nums) < 2:
            return nums[0]
        ans = float('-inf')
        for i in range(len(nums)):
            if nums[i] == 0:
                ans = max(ans,recursion(nums[:i]), recursion(nums[i+1:]))

        negatives, ln, rn = 0, len(nums)-1, 0
        for i in range(len(nums)):
            if nums[i] < 0:
                negatives += 1
                rn = i
                if ln < i:
                    ln = i

        if negatives%2 == 0:
            ans = 1
            print(nums)
            for n in nums:
                ans *= n
                print(ans)
        else:
            ans = max(ans,recursion(nums[:rn]), recursion(nums[ln:]))
        return ans
    
    return recursion(nums)

nums = [1,0,2,3,4,-2,-2]
print(maxProduct(nums))