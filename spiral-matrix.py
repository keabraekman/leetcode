# Given an m x n matrix, return all 
# elements of the matrix in spiral order.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# 3x3 = 3,2,2,1,1
# 4x3 = 4,2,3,1,2

# The idea is to go : up, right, down, left
# Each time, we diminish the size of the array 
# and append the elements into a result array
def spiralOrder(matrix):
    result, result_length, side = [], len(matrix) * len(matrix[0]), 0
    while len(result) < result_length:
        if side == 0: #UP
            for i in matrix[0]:
                result.append(i)
            matrix.pop(0)
        elif side == 1: #right
            for i in range(len(matrix)):
                result.append(matrix[i][len(matrix[i])-1])
                matrix[i].pop()
        elif side == 2: # down
            for i in reversed(matrix[len(matrix)-1]):
                result.append(i)
            matrix.pop()
        else: # left
            for i in range(len(matrix)):
                result.append(matrix[len(matrix)-1-i][0])
                matrix[len(matrix)-1-i].pop(0)
            side = -1
        side += 1
    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))