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


def canicas(M, v):
    n = v
    for i in range(len(M)):
        n = vec_matriz(n,M[i])
    return n 
    
