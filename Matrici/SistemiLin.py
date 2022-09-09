# Programma per ricavare soluzioni sistemi lineari - Riccardo Manoni
import Determinante

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

def main():
    

#print(ChangeColn([[0,2,3],[1,5,6],[1,8,9]], 1, [1,2,3]))
