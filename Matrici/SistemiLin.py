# modulo soluzioni sistemi lineari - Riccardo Manoni

from Inversa import MontanteBareiss
import Matrice, Determinante

def ChangeColn(matrix, index, vector):
    m2 = [row[:] for row in matrix]
    for row in range(len(matrix)): # scorro le righe con l'indice
        m2[row][index] = vector[row] # scrivo i nuovi valori del vettore colonna
    return m2

#Matrice.printMatrix(ChangeColn([[1,2,3],[2,2,1]], 0, [0,1,1]))

def Cramer(A, B): # A = matrice coefficienti, B = vettore termini noti
    solutions = []
    Det = Determinante.DetMatrice(A,0,0)
    for i in range(len(A)): # indice di dimensione matrice
        # determino le soluzioni date dalla Matrice dei coeff modificata / determinante
        #Matrice.printMatrix(ChangeColn(A, i, B))
        solutions.append(Determinante.DetMatrice(ChangeColn(A, i, B),0,0)/Det)
    return solutions

def InitSis():
    eq = input("Insert number of equations: ")
    var = input("Insert number of variables: ")
    if eq.isnumeric() and var.isnumeric():
        if eq > var:
            print("developing... sorry")
            return 0
        else:
            return Matrice.createMatrix(int(eq), int(var))
    else:
        print("value not allowed!")
        return InitSis()

def CalcSol(m):
    if m:
        x = len(m) # righe
        y = len(m[0]) # colonne
        if y > x+1:  # ES: righe:2 colonne:4
            Matrice.printMatrix(MontanteBareiss(m, 0))
        else: # risolvo con cramer
            a = Matrice.SubMatrix(m, 0, x, 0, y-1)
            b = Matrice.SubMatrix(m, 0, x, y-1, y)
            sol = Cramer(a, b)
            for i in range(len(sol)):
                print("x" + str(i) + ": " + str(sol[i]))


CalcSol(InitSis())
#print(ChangeColn([[0,2,3],[1,5,6],[1,8,9]], 1, [1,2,3]))
