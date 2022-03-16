# Given an m x n grid of characters board and a string word, return true if word exists 
# in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent 
# cells are horizontally or vertically neighboring. The same letter cell may not be used 
# more than once.

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true


# The idea is to check each letter one by one until we find the letter we are looking for



def next_letter(board, search, x, y):
    if x == 0:
        up = [None, None]
    else:
        up = [board[x-1][y], x-1, y]

    if x == len(board)-1:
        down = [None, None]
    else:
        down = [board[x+1][y], x+1, y]

    if y == 0:
        left = [None, None]
    else:
        left = [board[x][y-1], x, y-1]

    if y == len(board[0])-1:
        right = [None, None]
    else:
        right = [board[x][y+1], x, y+1]
    
    possibilities = [up[0], down[0], left[0], right[0]]
    full = [up, down, left, right]
    if search in possibilities:
        return full[possibilities.index(search)]
    else:
        return False

def exist(board, word):
    currentx, currenty = [], []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if word[0] == board[i][j]:
                currentx.append(i)
                currenty.append(j)
    if not currentx:
        return False

    print('currentx = ', currentx)
    print('currenty = ', currenty)
    for k in range(len(currentx)):
        for i in range(1,len(word)-1):
            print('k = ', k)
            print('x = ', currentx[k])
            print('y = ', currenty[k])
            print('word[i] = ', word[i])
            print(next_letter(board, word[i], currentx[k], currenty[k]))
            print()
            if next_letter(board, word[i], currentx[k], currenty[k]) != False:
                currentx[k], currenty[k] = next_letter(board, word[i], currentx[k], currenty[k])[1], next_letter(board, word[i], currentx[k], currenty[k])[2]
                # next_letter(board, word[i+1], currentx, currenty)
            else:
                break
        # print('i = ', i)
        if i == len(word)-1:
            return True
    return False






def exist(board, word):
    # Dimensions of board
    rows, cols = len(board), len(board[0])
    # We add the list of coordinates that we visit
    path = []

    # Backtracking function
    def dfs(r,c,i):
        # If we iterate through all the letters. Return true
        if i == len(word):
            return True
        # If the coordinates are wrong, if we've visited that coordinate before, or if 
        # the coordinates lead to the wrong letter
        if (r < 0 or c < 0 or r >= rows or c >= cols
        or word[i] != board[r][c] or [r,c] in path):
            return False
        
        # We add the coordinates to the path array
        path.append([r,c])
        # We recursively call the function four times (left right up down) and put the result as res
        # It will take on True unless they're all False. i+1 is because we are incrementing the letter we are 
        # looking for
        res = (dfs(r-1, c, i+1) or
        dfs(r+1, c, i+1) or
        dfs(r, c-1, i+1) or
        dfs(r, c+1, i+1))
        # Backtracking portion of the algorithm
        path.remove([r, c])
        # return result
        return res
    
    # Initiate the function with the first letter
    for c in range(cols):
        for r in range(rows):
            if dfs(r,c,0): return True
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))





def exist(board, word):
    rows, cols = len(board), len(board[0])
    path = []
    def dfs(r,c,i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or r >= rows or c >= cols
        or word[i] != board[r][c] or [r,c] in path):
            return False
        path.append([r,c])
        res = (dfs(r-1, c, i+1) or
        dfs(r+1, c, i+1) or
        dfs(r, c-1, i+1) or
        dfs(r, c+1, i+1))
        path.remove([r, c])
        return res
    for c in range(cols):
        for r in range(rows):
            if dfs(r,c,0): return True
    return False


def exist(board, word):
    rows, cols, path = len(board), len(board[0]), []
    def dfs(r,c,i):
        if i == len(word):
            return True
        if (r < 0 or r >= rows or c < 0 or c >= cols or word[i] != board[r][c] or [r,c] in path):
            return False
        path.append([r,c])
        res = (dfs(r-1,c,i+1) or dfs(r+1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1))
        path.remove([r,c])
        return res
    for c in range(cols):
        for r in range(rows):
            if dfs(r,c,0):
                return True
    return False





def exist(board, word):
    rows, cols, path = len(board), len(board[0]), []

    def dfs(r,c,i):
        if i == len(word):
            return True
        if (c < 0 or c >= cols or r < 0 or r >= rows or [r,c] in path or word[i] != board[r][c]):
            return False
        path.append([r,c])
        res = (dfs(r-1,c,i+1) or dfs(r+1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1))
        path.remove([r,c])
        return res
    
    for c in cols:
        for r in rows:
            if dfs(r,c,0):
                return True
    return False





def exist(board, word):
    rows, cols, path = len(board), len(board[0]), []
    def dfs(r,c,i):
        if i == len(word):
            return True
        if (c<0 or c>=cols or r<0 or r>=rows or board[r][c]!=word[i] or [r,c] in path):
            return False
        path.append([r,c])
        res = (dfs(r-1,c,i+1) or dfs(r+1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1))
        path.remove([r,c])
        return res
    for c in range(cols):
        for r in range(rows):
            if dfs(r,c,0):
                return True
    return False