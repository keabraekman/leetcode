
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

# print(threeSum(nums))




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





































# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, 
# and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Start with hashmap : 2d dict with two keys and the addition between those two

def threeSum(nums):
    dict_2d, ans = dict(), []
    for a in range(len(nums)):
        for b in range(len(nums)):
            if a < b:
                if nums[a] + nums[b] not in dict_2d:
                    dict_2d[nums[a]+nums[b]] = [[a,b]]
                else:
                    dict_2d[nums[a]+nums[b]].append([a,b])
    # print(dict_2d)
    for k in dict_2d:
        print(k, ' : ', dict_2d[k])

    for c in range(len(nums)):
        if -nums[c] in dict_2d:
            for i in range(len(dict_2d[-nums[c]])):
                if c not in dict_2d[-nums[c]][i]:
                    triplet = dict_2d[-nums[c]][i][:]
                    triplet.append(c)
                    ans.append(triplet)
    
    
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            ans[i][j] = nums[ans[i][j]]
    return ans














# Start by sorting the list
# Iterate through each element (not already visited)
# Use left and right pointers in sorted list
def threeSum(nums):
    nums.sort()
    a,l,r,ans = 0,1,len(nums)-1, []
    for a in range(len(nums)-2):
        if a==0 or a > 0 and nums[a] != nums[a-1]:
            l,r = a+1, len(nums)-1
            while l < r:
                if nums[a]+nums[l]+nums[r] == 0:
                    ans.append([nums[a], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l +=1
                elif nums[a] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
    return ans

# nums = [-2,0,0,2,2]
# print(threeSum(nums))







def threeSum(nums):
    nums.sort()
    res = []
    if len(nums)<3:
        return []
    for i in range(len(nums)-2):
        if i==0 or (nums[i] != nums[i-1]):
            l,r = i+1, len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and r>l:
                        l += 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
    return res



# nums = [-1,0,1,2,-1,-4]
nums = [-2,0,0,2,2]
print(threeSum(nums))