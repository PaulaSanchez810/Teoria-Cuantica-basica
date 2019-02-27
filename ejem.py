def multiplicaMatriz(A,B):
    for i in range(n):
      if columnas(A) == filas(B):
            C = creaMatriz(filas(A), columnas(B))
            for i in range(filas(C)):
                  for j in range(columnas(C)):
                        for k in range(columnas(A)):
                              C[i][j] += A[i][k] * B[k][j]
            return C
def vector_matriz(v, b):
    filasB = len(b)
    columnasA = len(v[0])
    if filasB == columnasA:
        filas = len(v)
        columnas = len(b[0])
        matriz = [[(0, 0)] * columnas for x in range(filas)]
        for i in range(0, filas):
            for j in range(0, columnas):
                for k in range(0, len(B)):
                    m = mult(v[i][k], b[k][j])
                    n = matriz[i][j]
                    matriz[i][j] = (m[0]+n[0], m[1]+n[1])
        return matriz
    else:
        return False
def Matriz_traspuesta(M):
    
      fila = len(M)
      columna = len(fila[0]) 
      T = creaMatriz(columna,fila)
      for i in range(columna):
            for j in range(fila):
                  T[i][j] = M[j][i]
      return T

def main():
    n=2
    L=[[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
       [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
       [(0,0),(1,0),(0,0),(0,0),(0,0),(1,0)]
       [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
       [(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)]
       [(1,0),(0,0),(0,0),(0,0),(1,0),(0,0)]
       ]
    V=[(6,0),(2,0),(1,0),(5,0),(3,0),(10,0)]
    V=Matriz_traspuesta(V)
    for i in range(1,n):
        vector_matriz(V,multiplicaMatriz(L))
        
main()
