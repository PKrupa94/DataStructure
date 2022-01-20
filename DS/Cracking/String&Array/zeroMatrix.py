def zeroMatrix(matrix):
    row = set()
    col = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
    for i in row:
        print('i', i)
        matrix[i] = [0 for i in range(len(matrix[0]))]
    for j in range(len(matrix)):
        for k in col:
            matrix[j][k] = 0
    return matrix


print(zeroMatrix([[1, 2], [4, 0], [6, 7]]))
