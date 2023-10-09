################################################################################
#Elaborador por: Miguel Alejandro Madrigal Ramírez
#Fecha de creación: 07/10/2023, 6:40 pm
#Última modificación:
#Versión: 3.11.5
################################################################################
#Importación de librerías
import random

#Definición de funciones con tuplas
def desgloseBilletes(recibo):
    """
    """
    billetes=[100,50,20,10,5,2,1]
    desglose=[]
    for i in range(len(billetes)):
        desglose.append(recibo//billetes[i])
        recibo=recibo%billetes[i]
    return print(desglose)

desgloseBilletes(1427)