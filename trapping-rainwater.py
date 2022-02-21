def trap(height):
    l, r, maxL, maxR, total = 0, len(height)-1, 0, 0, 0
    while l < r:
        if height[l] <= height[r]:
            maxL = max(maxL, height[l])
            total += maxL-height[l]
            l += 1
        else:
            maxR = max(maxR, height[r])
            total += maxR-height[r]
            r -= 1
    return total