import Determinante

def MontanteBareiss(m, k):
    if k < (len(m)): # indice per pivot
        #print("pivot " + str(k) + ": " + str(m[k][k]))
        #print(m)
        m2 = [row[:] for row in m] # copio la matrice m in m2 (python è stronzo)
        for i in range(k+1, len(m)): # indice per triangolare inferiore
            for j in range(k, len(m[0])):
                if k == 0:
                    m2[i][j] = m[k][k]*m[i][j]-m[i][k]*m[k][j]
                else:
                    m2[i][j] = (m[k][k]*m[i][j]-m[i][k]*m[k][j])/m[k-1][k-1]
        if k > 0:
            i = k-1 # indice per triangolare superiore
            while i >= 0:
                for j in range(i, len(m[0])):
                    #print("i: "+str(i)+" j: "+str(j))
                    m2[i][j] = (m[k][k]*m[i][j]-m[i][k]*m[k][j])/m[k-1][k-1]
                i -= 1
                #print(m2)
        return MontanteBareiss(m2, k+1)
    else:
        return ScalarByMatrix(SubMatrix(m, 0, len(m), len(m[0])-len(m), len(m[0])), 1/m[k-1][k-1])

#Matrice.printMatrix(MontanteBareiss([[1,2,3,1,0,0],[-3,-4,1,0,1,0],[2,1,2,0,0,1]], 0))

def MatriceInversa(matrice):
    if CheckInvertibility(matrice):
        print("Matrice Inversa: ")
        return MontanteBareiss(AddIdentityMatrix(matrice), 0)
    else:
        print("Matrice non invertibile")
        return -1

def ScalarByMatrix(matrix, factor):
    #print(matrix)
    m2 = []
    for row in matrix:
        v = []
        for coln in row:
            v.append(coln*factor)
        m2.append(v)
    return m2

def SubMatrix(matrix, initrow, endrow, initcoln, endcoln):
    x = len(matrix) # righe matrix
    y = len(matrix[0]) # colonne matrix
    m2 = [] # matrix di supporto
    if initrow <= x and endrow <= x and initrow < endrow:
        if initcoln <= y and endcoln <= y and initcoln < endcoln:
            for i in range(initrow, endrow, 1):
                v = []
                for j in range(initcoln, endcoln, 1):
                    #print("i: "+str(i)+" j: "+str(j))
                    v.append(matrix[i][j])
                m2.append(v)
            return m2
        else:
            print("indexes not allowed!")
            return -1
    else:
        print("indexes not allowed!")
        return -1
#printMatrix(SubMatrix([[1,2,3],[-3,-4,1],[2,1,2]],0,1,0,1))

def IdentityMatrix(n):
    matrix = []
    for i in range(n):
        v = []
        for j in range(n):
            if i == j:
                v.append(1)
            else:
                v.append(0)
        matrix.append(v)
    return matrix

def AddIdentityMatrix(matrix):
    identity = IdentityMatrix(len(matrix))
    for index in range(len(matrix)):
        matrix[index].extend(identity[index])
    return matrix

def CheckInvertibility(matrix):
     return 1 if Determinante.DetMatrice(matrix, 0,0) != 0 else 0
