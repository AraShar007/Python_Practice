X = [[1,3,9],
      [3, 7, 6],
      [6, 8, 9]]
Y = [[1, 7, 1],
    [6, 7, 3],
    [5, 5, 9]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for r in result:
    print(r)