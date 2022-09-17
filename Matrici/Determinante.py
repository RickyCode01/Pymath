# modulo per calcolo determinante - Riccardo Manoni

def Det2x2(matrice):
    return (matrice[0][0]*matrice[1][1])-(matrice[0][1]*matrice[1][0])

def Det3x3(matrice):
    return (matrice[0][0]*matrice[1][1]*matrice[2][2]+matrice[0][1]*matrice[1][2]*matrice[2][0]+
        matrice[1][0]*matrice[2][1]*matrice[0][2])-(matrice[2][0]*matrice[1][1]*matrice[0][2]+
        matrice[2][1]*matrice[1][2]*matrice[0][0]+matrice[1][0]*matrice[0][1]*matrice[2][2])

def MatriceCofattori(matrice, riga, colonna):
    mcoff = []
    if riga <= len(matrice)-1 and colonna <= len(matrice[0])-1:
        for righe in matrice:
            if righe != matrice[riga]:
                tmp = []
                for indice in range(len(righe)):
                    if indice != colonna:
                        tmp.append(righe[indice])
                mcoff.append(tmp)
        return mcoff
    else:
        print("indici fuori scala")
        return -1

def DeterminanteLaplace(matrice, sviluppo, indice, determinante):
    #print(matrice)
    if len(matrice) == 2:
        return Det2x2(matrice)
    else:
        if indice <= len(matrice):
            if sviluppo == 1: #sviluppo rispetto alla colonna dell'indice
                for nrighe in range(len(matrice)):
                    determinante += pow(-1,nrighe+indice) * matrice[nrighe][indice] * DeterminanteLaplace(MatriceCofattori(matrice, nrighe, indice), sviluppo, indice-1, determinante)
            elif sviluppo == 0:
                for ncoln in range(len(matrice[0])):
                    determinante += pow(-1,ncoln+indice) * matrice[indice][ncoln] * DeterminanteLaplace(MatriceCofattori(matrice, indice, ncoln), sviluppo, indice-1, determinante)
            else:
                print("sviluppo: 0 per riga, 1 per colonna")
                determinante = -1
            return determinante
        else:
            print("indice sviluppo fuori range")
            return -1

def DetMatrice(matrice, sviluppo, indice):
    return DeterminanteLaplace(matrice, sviluppo, indice, 0)
