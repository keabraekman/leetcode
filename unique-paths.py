# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.


def uniquePaths(m, n):
    grid = []
    # firstRow = [1]*n
    # grid.append(firstRow)
    for i in range(m):
        row = [1]*n
        grid.append(row)
        for j in range(n):
            if i > 0 and j < n-1:
                grid[i][j] = grid[i-1][j] + grid[i][j+1]
    return grid


grid = uniquePaths(3,7)

for i in range(len(grid)):
    print(grid[i])


def uniquePaths(m, n):
    row = [1]*n
    for i in range(m-1):
        newRow = [1]*n
        for j in range(n-2,-1,-1):
            newRow[j] = newRow[j+1]+row[j]
        row = newRow
    return row[0]














def uniquePaths(m,n):
    grid = []
    for i in range(m):
        grid.append([1]*n)
    
    for i in range(m-2,-1,-1):
        for j in range(n-2, -1, -1):
            grid[i][j] = grid[i+1][j] + grid[i][j+1]
    return grid[0][0]

print(uniquePaths(7,3))