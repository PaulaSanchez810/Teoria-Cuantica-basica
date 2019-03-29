def mult(a, b):
    r = (a[0] * b[0]) - (a[1] * b[1])
    i = (a[1] * b[0]) + (b[1] *a[0])
    rta = (r,i)
    return rta


def Tensor(A,B):
    filasA = len(A)
    columnasA = len(A[0])
    filasB = len(B)
    columnasB = len(B[0])
    for i in range(filasA):
        for j in range(columnasA):
            C = []
            for x in range(filasB):
                for y in range(columnasB): C.append(mult(A[i][j], B[x][y]))
            A[i][j] = C
    return A


def vec_matriz(v, b):
    filasB = len(b)
    columnasA = len(v[0])
    if filasB == columnasA:
        filas = len(v)
        columnas = len(b[0])
        matriz = [[(0, 0)] * columnas for x in range(filas)]
        for i in range(0, filas):
            for j in range(0, columnas):
                for k in range(0, len(b)):
                    m = mult(v[i][k], b[k][j])
                    n = matriz[i][j]
                    matriz[i][j] = (m[0]+n[0], m[1]+n[1])
        return matriz
    else:return False


def matriz_multiplicacion(A, B):
    filasB = len(B)
    columnasA = len(A[0])
    if filasB == columnasA:
        filas = len(A)
        columnas = len(B[0])
        matriz = [[(0, 0)] * columnas for x in range(filas)]
        for i in range(0, filas):
            for j in range(0, columnas):
                for k in range(0, len(B)):
                    m = mult(A[i][k], B[k][j])
                    n = matriz[i][j]
                    matriz[i][j] = (m[0]+n[0], m[1]+n[1])
        return matriz
    else:
        print("La dimensión de la matriz es incorrecta, inténtalo de nuevo.")
        return False


def transpose(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    return [[matriz[j][i] for j in range(filas)] for i in range(columnas)]


def canicas(M, N, v):
    n = M
    while N != 0:
        f = matriz_multiplicacion(n, M)
        n = f
        N -= 1
    return matriz_multiplicacion(n, transpose(v))


def balas(M, N, v):
    n = M
    while N != 0:
        f = matriz_multiplicacion(n, M)
        n = f
        N -= 1
    return matriz_multiplicacion(n, transpose(v))



def Doble_rendija(M, N):
    n = M
    while N != 0:
        f = matriz_multiplicacion(n, M)
        n = f
        N -= 1
    f = M
    for i in range(len(M)):
        for j in range(len(M[0])):
            h = ((M[i][j][0] ** 2) + (M[i][j][1] ** 2))**0.5
            f[i][j] = h
    return f
