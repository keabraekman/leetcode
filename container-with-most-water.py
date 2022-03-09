import math

height = [1,8,6,2,5,4,8,3,7]

# INEFFICIENT SOLUTION
def maxArea(height):
    areas = []
    for i in range(len(height)):
        areas_local = []
        for j in range(len(height)):
            area = min([height[i], height[j]]) * (abs(i-j))
            areas_local.append(area)
        areas.append(max(areas_local))
    print(areas)
    return max(areas)

# print(maxArea(height))


def maxArea(height):
    left = 0
    right = len(height)-1
    area = 0
    while(left < right):
        area = max(area, (right-left) * min(height[left], height[right]))
        if(height[left] < height[right]):
            left += 1
        else :
            right -= 1
    return area


print(maxArea(height))














def maxArea(height):
    l,r,ans = 0, len(height)-1, 0
    while l < r:
        ans = max(ans, (r-l)*min(height[l],height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return ans


height = [1,8,6,2,5,4,8,3,7]

print(maxArea(height))