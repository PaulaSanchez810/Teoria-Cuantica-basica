def hermitiana(A):
    filasA = len(A)
    columnasA = len(A[0])
    if filasA == columnasA:
        Ac = transpose(A)
        Ac = conj(Ac)
        if Ac == A:
            return True
        else:
            return False
    else:
        return False



    
def evaluar (A,V):
    new_v=[]
    if hermitiana(A)==True:
        if len(A)==len(V):
            R=vector_matriz(V,A)
        for i in range(len(R)):
            R[i]=R[i]*V[i]
        escalar=R
        return escalar 
##identidad
##escalarporlaidentidad
##restar la orinal por la hermitiana origianl 

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
    

def resta_matriz():
    

def matriz_identidad(A):
    for i in range(len(A)):
        for j in range(len(A)):
            

            
            
            
    
    
    
    
    

        
        
        
    
    
