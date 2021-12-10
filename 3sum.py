
def threeSum(nums):
    triplets = []
    required2d = []
    used_triplets = []
    for i in range(len(nums)):
        required = []
        for j in range(len(nums)):
            if(i == j):
                required.append(None)
            else:
                required.append(-(nums[i] + nums[j]))
        required2d.append(required)
    
    for x in range(len(required2d)):
        for y in range(len(required2d[0])):
            if(required2d[x][y] in nums):
                z = nums.index(required2d[x][y])
                if(z not in [x,y] and [nums[x],nums[y],nums[z]] not in used_triplets):
                    triplets.append([nums[x], nums[y], nums[z]])
                    used_triplets += ([nums[x],nums[y],nums[z]], [nums[x],nums[z],nums[y]], [nums[y],nums[x],nums[z]], [nums[y],nums[z],nums[x]], [nums[z],nums[y],nums[x]], [nums[z],nums[x],nums[y]])
    return triplets
nums = [-1,0,1,2,-1,-4]

# print(threeSum(nums))



def threeSum(nums):
    res = []
    nums.sort()
    # we run through all numbers except for the last two since we're looking for triplets and
    # i is the lowest number
    for i in range(len(nums)-2):
        # If not the first element of the list and the preceding int is different, we continue
        # Else, we ignore. This is to avoid duplicate ints in the list.
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # i is the minimum number index, l, and r are the other two index
        # 
        l = i+1
        r = len(nums)-1
        # We start at the far left and right (right of i)
        # And work our way to the middle
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            # If sum < 0, increase left
            if s < 0:
                l +=1 
            # If sum > 0, decrease right
            elif s > 0:
                r -= 1
            # if zero, append the solution
            else:
                res.append((nums[i], nums[l], nums[r]))
                # This is to avoid duplicates again. 
                # If the l+1 number is the same as l, ignore it
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                # Increment for next int
                # Keep in mind that the entire while loop is in the for loop
                # There may be more than one solution. But we know that it has
                # to be to the left of l and to the right of r
                l += 1
                r -= 1
    return res

print(threeSum(nums))




class Solution:
    def threeSum(nums):
        nums.sort()
        triplets = []
        for i in range(len(nums) - 2):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                s = nums[i] + nums[left] + nums[right]
                if(s > 0):
                    right -= 1
                elif(s < 0):
                    left += 1
                else:
                    triplets.append((nums[i], nums[left], nums[right]))
                    while(left < right and nums[left] == nums[left+1]):
                        left += 1
                    while(left < right and nums[right] == nums[right-1]):
                        right -= 1
                    left += 1
                    right -= 1
        return triplets