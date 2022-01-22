import numpy as np

matrix = np.zeros((21,21),  dtype=np.int64)      # defined 20x20 matrix

for i in range(0,21):
    matrix [i][0] = 1
    matrix [0][i] = 1

for i in range(0,21):
    matrix [i][0] = 1
    matrix [0][i] = 1


for j in range(0, 20):
    for i in range(0, 20):
        matrix [i+1][j+1] = matrix [i][j+1] + matrix [i+1][j]


print(matrix[20][20])