import math

# height = [1,8,6,2,5,4,8,3,7]
height = [1,2,4,3]

# def maxArea(height):
#     areas = []
#     for i in range(len(height)):
#         areas_local = []
#         for j in range(len(height)):
#             area = min([height[i], height[j]]) * (abs(i-j))
#             areas_local.append(area)
#         areas.append(max(areas_local))
#     print(areas)
#     return max(areas)

# print(maxArea(height))





def maxArea(height):
    left = 0
    right = 0
    l = 0
    r = 0
    for i in range(len(height)):
        if(left+i<height[i]):
            left = height[i]
            l = i
    for i in range(len(height)):
        if(right+i<height[len(height)-1-i]):
            right = height[len(height)-1-i]
            r = len(height)-1-i
    print(l)
    print(r)
    return (abs(r-l) * min([left, right]))

print(maxArea(height))

