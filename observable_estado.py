def complejo(x):
    return complex(x[0], x[1])


def prube(a):
    x = a[0] - 0.1
    y = a[1]
    if a[1] > 0:
        y -= 0.1
    r = (x, y)
    return r


def mult(a, b):
    r = (a[0] * b[0]) - (a[1] * b[1])
    i = (a[1] * b[0]) + (b[1] *a[0])
    rta = (r,i)
    return rta


def norma_vector_complejo(v):
    cont = 0
    for i in range(len(v)):
        cont += (v[i][0] ** 2 + v[i][1] ** 2)
    return round((cont**0.5), 4)


def trans(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    return [[matriz[j][i] for j in range(filas)] for i in range(columnas)]


def conj(A):
    filas = len(A)
    columnas = len(A[0])
    for i in range(filas):
        for j in range(columnas):
            b = A[i][j]
            x = b[0]
            y = b[1]*-1
            m = (x,y)
            A[i][j] = m
    return A


def matriz_mult(A, B):
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


def resta(a, b):
    R = [[(0, 0)] * len(a) for x in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            R[i][j] = (a[i][j][0] - b[i][j][0], a[i][j][1] - b[i][j][1])
    return R


def hermitiana(A):
    filasA = len(A)
    columnasA = len(A[0])
    if filasA == columnasA:
        Ac = trans(A)
        Ac = conj(Ac)
        if Ac == A:
            return True
        else:
            return False
    else:
        return False


def particula(v):
    i = 1
    norm = norma_vector_complejo(v)
    proba = (i/(norm**2))
    return round(proba, 6)


def normalizar(v):
    i = 1
    norm = norma_vector_complejo(v)
    new = [[]]
    for i in range(len(v)):
        a = (1/norm) * v[i][0]
        b = (1/norm) * v[i][1]
        new[0].append((round(a, 5), round(b, 5)))
    return new


def spin(v):
    norm = norma_vector_complejo(v)**2
    up = v[0][0]**2 + v[0][1]**2
    dw = v[1][0]**2 + v[1][1]**2
    x = round((up/norm), 2)
    y = round((dw/norm), 2)
    re = (x, y)
    return re


def ident(c, M):
    R = [[(0, 0)] * len(M) for x in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M)):
            if i == j:
                R[i][j] = (c, 0)
    return R
