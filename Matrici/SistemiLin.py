# modulo soluzioni sistemi lineari - Riccardo Manoni

from Inversa import MontanteBareiss
import Matrice, Determinante

def ChangeColn(matrix, index, coln):
    m2 = [row[:] for row in matrix]
    for row in range(len(matrix)): # scorro le righe con l'indice
        m2[row][index] = coln[row] # scrivo i nuovi valori della colonna
    return m2

def Cramer(A, B): # A = matrice coefficienti, B = vettore termini noti
    solutions = []
    Det = Determinante.DetMatrice(A,0,0)
    for i in range(len(A)): # indice di dimensione matrice
        # determino le soluzioni date dalla Matrice dei coeff modificata / determinante
        solutions.append(Determinante.DetMatrice(ChangeColn(A, i, B),0,0)/Det)
    return solutions

def initSis():
    eq = input("Insert number of equations: ")
    var = input("Insert number of variables: ")
    return Matrice.createMatrix(int(eq), int(var))

def CalcSol(m):
    Matrice.printMatrix(MontanteBareiss(m, 0))

CalcSol([[1,2,3],[2,2,1]]) # SOL -> x=-2 , y=5/2
#print(ChangeColn([[0,2,3],[1,5,6],[1,8,9]], 1, [1,2,3]))
