# creazione Matrici python -> Riccardo Manoni

def createMatrix(dimX, dimY):
    matrix = []
    print("TIP => x,y,z for 3 element vector")
    matrix = recursiveMatrix(dimX, dimY, dimX, matrix)
    printMatrix(matrix)
    return matrix

def recursiveMatrix(dimX, dimY, count, matrix):
    if dimX > 0:
        rows = input("insert " + str(count+1-dimX) + "st row:")
        #print(row.count(','))
        if Validation(rows.split(","), dimY): # controllo numero elementi
            tmp = []
            for element in rows.split(','):
                tmp.append(int(element))
            matrix.append(tmp)
            return recursiveMatrix(dimX-1, dimY, count, matrix)
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
        if dim[0].isnumeric() and dim[1].isnumeric():
            return createMatrix(int(dim[0]), int(dim[1]))
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

def Validation(sarray, lenght):
    return 1 if len(sarray) == lenght else 0

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

#printMatrix(Transpose([[1,2,3],[4,5,6],[7,8,9]]))
