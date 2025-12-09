A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
resultado = [[0, 0],
             [0, 0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            resultado[i][j] += A[i][k] * B[k][j]
print("Producto de matrices:")
for fila in resultado:
    print(fila)   