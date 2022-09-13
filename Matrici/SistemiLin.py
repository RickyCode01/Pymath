# Programma per ricavare soluzioni sistemi lineari - Riccardo Manoni
import Inversa, Determinante

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

def SisMatrix(Matrix, n, m, count):
    if m == 0:
        return Matrix
    else:
        v = []
        rows = input("Insert " + str(count-m) + "st row: ")
        if Validation(rows.split(","), n):
            for num in rows.split(","):
                v.append(num)
            Matrix.append(v)
            return SisMatrix(Matrix, n, m-1, count)
        else:
            print("Not Allowed!" + "TIP(3 var) -> x,y,z")
            return SisMatrix(Matrix, n, m, count)

def init():
    var = input("Insert number of variables: ")
    eq = input("Insert number of equations: ")
    return SisMatrix([], int(var), int(eq), int(eq)+1)

def Validation(sarray, lenght):
    return 1 if len(sarray) == lenght else 0


print(init())
#print(ChangeColn([[0,2,3],[1,5,6],[1,8,9]], 1, [1,2,3]))
