
# C[i][j]=A[i][j]+B[i][j]
def matrix_addition(mat1, mat2):
    result = [[mat1[i][j] + mat2[i][j]
               for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return result


# C[i][j]=A[i][j]-B[i][j]
def matrix_subtracting(mat1, mat2):
    result = [[mat1[i][j] - mat2[i][j]
               for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return result


# The product of two matrices A (m x n) and B (n x p) is a matrix C (m x p)
# C[i][j] = sum(A[i][k]*B[k][j]) (k = range (1,n))
# A = [           B = [
#     [1, 2, 3]       [7, 8]
#     [4, 5, 6]       [9, 10]
#     ]               [11, 12]
#                     ]
# 
# C = [                                      ==>  C = [
#         [(1*7+2*9+3*11), (1*8+2*10+3*12)],              [58, 64]
#         [(4*7+5*9+6*11), (4*8+5*10+6*12)]               [139, 154]           
# ]                                                   ]

def matrix_multiplication(mat1, mat2):
    result = [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2)))
               for j in range(len(mat2[0]))] for i in range(len(mat1))]
    return result


# T[i][j]=A[j][i]
def transpose_matrix(mat):
    result = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    return result


# Example usage:
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_matrix = matrix_addition(matrix1, matrix2)
print("Matrix Addition Result:")
for row in result_matrix:
    print(row)


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_matrix = matrix_subtracting(matrix1, matrix2)
print("Matrix Subtraction Result:")
for row in result_matrix:
    print(row)

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]
result_matrix = matrix_multiplication(matrix1, matrix2)
print("Matrix Multiplication Result:")
for row in result_matrix:
    print(row)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose_matrix(matrix)
print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)
