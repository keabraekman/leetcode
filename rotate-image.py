# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.


# Input: matrix = [[1,2,3],
#                  [4,5,6],
#                  [7,8,9]]

# Output: [        [7,4,1],
#                  [8,5,2],
#                  [9,6,3]]

# You do not return anything. You need to modify the matrix in place!!

# Solution that returns a new matrix
def rotate(matrix):
    answer = []
    for y in range(len(matrix)):
        # 20, 10, 00, 21, 11, 01, 22, 12, 02, xy
        row = []
        for i in range(len(matrix)):
            x = len(matrix) - 1 - i
            row.append(matrix[x][y])
        answer.append(row)
    return answer


test = [[1,2,3],[4,5,6],[7,8,9]]

# print(rotate(test))



# Input: matrix = [[1,2,3],
#                  [4,5,6],
#                  [7,8,9]]

# Output: [        [7,4,1],
#                  [8,5,2],
#                  [9,6,3]]


# Input: matrix = [[1,2,3,4],
#                  [5,6,7,8],
#                  [9,0,1,2],
#                  [3,4,5,6]]

# Output: matrix = [[3,9,5,1],
#                   [4,0,6,2],
#                   [5,1,7,3],
#                   [6,2,8,4]]

def rotate(matrix):
    # Invert the list first 
    n = len(matrix)
    for i in range(int(n/2)):
        matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
    for i in range(n):
        for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix











def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
    
    for i in range(n):
        for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    





matrix = [[1,2,3],[4,5,6],[7,8,9]]



print(rotate(matrix))