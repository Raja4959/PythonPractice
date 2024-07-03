# Bitmap Holes : Statememt

# Have the function BitmapHoles(strArr) take the array of strings stored in strArr,
# which will be a 2D matrix of 0 and 1's, and determine how many holes, or contiguous regions of 0's, exist in the matrix.
# A contiguous region is one where there is a connected group of 0's going in one or more of four directions: up, down, left, or right.
# For example: if strArr is ["10111", "10101", "11101", "11111"], then this looks like the following matrix:

# 1 0 1 1 1
# 1 0 1 0 1
# 1 1 1 0 1
# 1 1 1 1 1

# For the input above, your program should return 2 because there are two separate contiguous regions of 0's,
# which create "holes" in the matrix. You can assume the input will not be empty.

def count_bitmap_holes(str_matrix):
    matrix = [list(row) for row in str_matrix]
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for j in range(cols)] for i in range(rows)]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] != '0' or visited[r][c]:
            return
        visited[r][c] = True
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    res = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '0' and not visited[r][c]:
                dfs(r, c)
                res += 1
    
    return res


input = ["10111", "10101", "11101", "11111"]

print(count_bitmap_holes(input))
