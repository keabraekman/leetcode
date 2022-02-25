# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


from lib2to3.pygram import python_symbols


def productExceptSelf(nums):
    pre, post, ans = [nums[0]]*len(nums), [nums[-1]]*len(nums), [0]*len(nums)
    for i in range(1,len(nums)):
        pre[i] = pre[i-1]*nums[i]
        post[len(nums)-i-1] = post[len(nums)-i]*nums[len(nums)-i-1]  
    ans[0], ans[-1] = post[1], pre[len(nums)-2]
    for i in range(1,len(nums)-1):
        ans[i] = pre[i-1] * post[i+1]
    return ans


def productExceptSelf(nums):
    pre, post, ans = 1,1,[1]*len(nums)
    for i in range(len(nums)):
        ans[i] = pre
        pre *= nums[i]
    for i in range(len(nums)):
        ans[len(nums)-1-i] *= post
        post *= nums[len(nums)-1-i]
    return ans

    
print(productExceptSelf([1,2,3,4]))