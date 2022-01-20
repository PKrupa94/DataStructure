def rotateMatrix(matrix):
    output = [[0 for i in range(len(matrix))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            output[j][len(matrix)-i-1] = matrix[i][j]
    return output


print(rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotateMatrix([[1, 2], [3, 4]]))
