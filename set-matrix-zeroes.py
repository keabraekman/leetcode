# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]



def setZeroes(matrix):
    x, y = [], []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if i not in y:
                    y.append(i)
                if j not in x:
                    x.append(j)
    for k in range(len(y)):
        for i in range(len(matrix[0])):
            matrix[y[k]][i] = 0

    for k in range(len(x)):
        for i in range(len(matrix)):
            matrix[i][x[k]] = 0
    return matrix


matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix))