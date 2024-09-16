''' Programma per ricavare matrice trianngolare con metodo di gauss (eliminazione gaussiana)
una matrice triangolare sup è un tipo di matrice quadrata dove a(i,j) = 0 per i>j '''
''' L'eliminazione gaussiana è un processo che può essere visto come la fattorizzazione
di una matrice A come prodotto di due matrici triangolari: La matrice L triangolare inferiore 
e la matrice U Triangolare superiore '''

from Matrice import printMatrix, InitMatrix

# return identity matrix of nxn dimensions
def IdentityMatrix(n):
	I = [] # final matrix
	for i in range(n):
		row = [] # matrix rows
		for j in range(n):
			row.append(1 if i == j else 0)
		I.append(row)
	return I

def GaussianElimination(A, n)-> list:
	L = IdentityMatrix(n)
	for k in range(n-1): # indice per scorrere colonne diagonale (pivot)
		for i in range(k+1, n): # indice righe sotto diagonale
			L[i][k] = A[i][k]/A[k][k];
			# print(c);
			for j in range(k+1, n): # indice colonne dopo colonna i(diagonale+1 -> n)
				A[i][j] = A[i][j] - L[i][k] * A[k][j];
			# printMatrix(A, n, n, str(i))
			A[i][k] = 0; # azzera elementi sotto colonna pivot
	return [L, A]


# m = [[1, -2 , -1],[4, -5, -4],[-3, 21, 6]]
m = InitMatrix("A")
length = len(m)
factorization = GaussianElimination(m, length)
printMatrix(factorization[0], length, length, "L")
printMatrix(factorization[1], length, length, "U")

# Matrice.printMatrix(m)
# m = GaussianElimination(m, 3)
# Matrice.printMatrix(m);







