# creazione Matrici python -> Riccardo Manoni

from Determinante import DetMatrice
import Inversa

def createMatrix(dimX, dimY):
    matrix = []
    print("TIP => x,y,z for 3 element vector")
    matrix = recursiveMatrix(dimX, dimY, 1, matrix)
    printMatrix(matrix)
    return matrix

def recursiveMatrix(dimX, dimY, count, matrix):
    if dimX > 0:
        row = input("insert " + str(count) + "st row:")
        #print(row.count(','))
        if len(row) == (2*dimY-1) and row.count(',') == dimY-1: # controllo lunghezza riga e numero virgole
            tmp = []
            for element in row.split(','):
                tmp.append(conv_check_Int(element))
            matrix.append(tmp)
            return recursiveMatrix(dimX-1, dimY, count+1, matrix)
        else:
            print('Not Allowed Try x,y,...,z ')
            return recursiveMatrix(dimX, dimY, count, matrix)
    else:
        return matrix

def InitMatrix():
    val = input("Insert Vector Dimentions(X,Y):")
    if "," in val and len(val) == 3:
        dim = val.split(",")
        #print(dim[1] + " => " + str(type(conv_check_Int(dim[1]))))
        if conv_check_Int(dim[0]) > 0 and conv_check_Int(dim[1]) > 0:
            return createMatrix(conv_check_Int(dim[0]), conv_check_Int(dim[1]))
        else:
            print("value not allowed")
            InitMatrix()
    else:
        print("value not allowed")
        InitMatrix()

def printMatrix(matrix):
    if matrix != -1:
        print("\t")
        for row in range(len(matrix)):
            print(matrix[row])
        print("\t")

def conv_check_Int(value): # check if string value is a number (if not return -1)
    #print(value + " => " + str(type(value)))
    return int(value) if value.isnumeric() else -1

def checkSquareMatrix(matrix):
    if len(matrix) > 1 and len(matrix) == len(matrix[0]):
        return 1
    else:
        return 0

def Transpose(matrix):
    mt = [row[:] for row in matrix]
    for row in range(len(matrix)):
        for coln in range(len(matrix)):
            # scambio gli elementi delle righe con quelli delle colonne
            mt[row][coln] = matrix[coln][row]
    return mt

#printMatrix(Transpose([[1,2,3],[4,5,6],[7,8,9]]))

def main():
    in1 = input("create new vector?(Y/N):").upper()
    if "Y" in in1:
        matrix = InitMatrix()
        if checkSquareMatrix(matrix):
            in2 = input("1 -> Determiante, 2 -> Inversa: ").upper()
            if "1" in in2:
                print("Determinate: " + str(DetMatrice(matrix, 0, 1)))
            elif "2" in in2:
                printMatrix(Inversa.MatriceInversa(matrix))
            else:
                return 0
    elif "N" in in1:
        print("Goodbye!")
    else:
        print("value not allowed")
        main()

#main()
