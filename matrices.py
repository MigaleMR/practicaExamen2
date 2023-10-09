#Matrices
import random
def verificarDiagonalSuperior(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                if matriz[i][j] == 0:
                    return print(False)
    return print(True)

verificarDiagonalSuperior([[1,2,3],[0,12,6],[0,0,-3]])

def multiplicarMatrices(matriz1, matriz2):
    """
    """
    if len(matriz1[0]) != len(matriz2):
        raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz")

    # Inicializa una matriz resultado con ceros
    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]

    # Realiza la multiplicación de matrices
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return print(resultado)

multiplicarMatrices([[2,4,6],[1,2,3],[0,3,6]],[[15,2,3], [1,2,3],[2,4,6]])