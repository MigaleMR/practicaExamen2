################################################################################
#Elaborador por: Miguel Alejandro Madrigal Ramírez
#Fecha de creación: 28/09/2023, 11:40 pm
#Última modificación:
#Versión: 3.11.5
################################################################################
import re
import random
def esPar(num):
      """
      Función que recibe un número entero y devuelve True si es par y False si es
      impar.
      """
      if num%2==0:
         return True
      else:
         return False
def analizarCadena(txt):
    """
    Función que analiza una cadena de texto y devuelve una lista con los
    caracteres que la componen.
    """
    vocales=consonantes=espacios=otros=numeros=0
    for i in range(len(txt)):
        if txt[i].isdigit():
           numeros+=1
        elif txt[i].isalpha():
           if txt[i] in "aeiouAEIOU":
              vocales+=1
           else:
              consonantes+=1
        elif txt[i].isspace():
              espacios+=1
        else:
            otros+=1  
    lista=["Vocales: ",vocales, "Consonantes: ",consonantes, "Espacios: ", espacios ,"Simbolos: ",otros,"Numeros: ",numeros]
    return print(lista)

def gordoNavidenno(listaGordo):
      """
      """
      gordoPar=[]
      for i in range(len(listaGordo)):
         if lista[i]%2==0:
               gordoPar.append(lista[i])  
      return print(gordoPar)

def indicarParidad(lista):
    """
    """
    nuevaLista=[]
    print(lista)
    for i in range(len(lista)):
        if lista[i]%2==0:
            nuevaLista.append(1)
        else:
            nuevaLista.append(0) 
    return print(nuevaLista)
listaCarnet=[2018012345, 2023012345, 2021019876, 2021021234, 2019012345, 2018025678, 2022012345]
def revisarCarnet(listaCarnet):
   """
   """
   carnet2018=carnet2019=carnet2020=carnet2021=carnet2022=carnet2023=0
   for i in listaCarnet:
      if str(i)[0:4]=="2018":
         carnet2018+=1
      elif str(i)[0:4]=="2019":
         carnet2019+=1
      elif str(i)[0:4]=="2020":
         carnet2020+=1
      elif str(i)[0:4]=="2021":
         carnet2021+=1
      elif str(i)[0:4]=="2022":
         carnet2022+=1
      elif str(i)[0:4]=="2023":
         carnet2023+=1
   return print("\nDel 2018: ",carnet2018,"\nDel 2019: ",carnet2019,"\nDel 2020: ",carnet2020,"\nDel 2021: ",carnet2021,"\nDel 2022: ",carnet2022,"\nDel 2023: ",carnet2023)

def notasImaginarias(notas):
   """
   """
   print(notas)
   reprobo=reposicion=aprobo=promedio=promedioTotal=0
   for i in range(len(notas)):
      if notas[i]<60:
            reprobo+=1
      elif notas[i]>=60 and notas[i]<70:
            reposicion+=1  
      elif notas[i]>=70:
            aprobo+=1
      promedio+=notas[i]
   promedioTotal=promedio/len(notas)
   return print("Estudiantes reprobados: ",reprobo,"\nEstudiantes en reposicion: ",reposicion,"\nEstudiantes aprobados: ",aprobo,"\nPromedio de notas: ",promedioTotal)

def calificarEdades(edades):
   """
   """
   print(edades)
   bebe=ninno=adolescente=adultoJoven=adultoMayor=0
   for i in range(len(edades)):
      if edades[i]<=3:
         bebe+=1
      elif edades[i]>3 and edades[i]<=12:
         ninno+=1  
      elif edades[i]>12 and edades[i]<=21:
         adolescente+=1
      elif edades[i]>21 and edades[i]<=60:
         adultoJoven+=1
      else:
         adultoMayor+=1
   return print("Bebes: ",bebe,"\nNiños: ",ninno,"\nAdolescentes: ",adolescente,"\nAdultos jovenes: ",adultoJoven,"\nAdultos mayores: ",adultoMayor)

def conocerEdades(edades):
   """
   """
   restantes=[]
   print(edades)
   edadMayor=edades[0]
   edadMenor=edades[0]
   for i in edades:
      if i<edadMenor:
         edadMenor=i
      elif i>edadMayor:
         edadMayor=i
      else:
         restantes.append(i)   
   for edad in edades:
       if edad<edadMayor and edad>edadMenor:
         restantes.append(edad)
   comprobarBis=2023-edadMayor
   if comprobarBis%4==0 or comprobarBis%400==0:
      txt="El año es bisiesto"
   else:
      txt="El año no es bisiesto"
   return print("Edad mayor:" ,edadMayor,", y nació en el año:",2023-edadMayor,txt,"\nEdad menor:",edadMenor, ", y nació en el año:",2023-edadMenor, "\nEntre la edad mayor y la menor hay una diferencia de:",edadMayor-edadMenor,"Y entre ellos estan las edades:",restantes)

def productoCartesiano(lista1,lista2):
   """
   """
   lista3=[]
   for i in range(len(lista1)):
      for j in range(len(lista2)):
         lista3.append((lista1[i],lista2[j]))
   return print(lista3)

def eliminarEspacios(txt):
   """
   """
   txt=txt.replace(" ","")
   return print(txt)

def buscarVirus(listaVirus, indice):
   """
   """
   for i in range(len(listaVirus)):
      if i==indice:
         listaVirus[i]="Virus"
   return print(listaVirus)
"""
edadesConocidos=int(input("Digite la cantidad de edades a ingresar: "))
edades=[int(input("Digite la edad: ")) for _ in range(edadesConocidos)]
cantidadEdades=int(input("Digite la cantidad de edades a ingresar: "))
edades=[random.randint(0,100) for _ in range(cantidadEdades)]
notas=[random.randint(0,100) for _ in range(10)]
listaGordo=[random.randint(0,99) for _ in range(5)]
lista=[random.randint(0,99) for _ in range(5)]
lista1=[1,2,3]	
lista2=[4,5,6]
txt= "asdlk;ifhn 11;z//123daslkn231"
revisarCarnet(listaCarnet)
analizarCadena(txt)
indicarParidad(lista)
gordoNavidenno(listaGordo)
notasImaginarias(notas)
calificarEdades(edades)
conocerEdades(edades)
productoCartesiano(lista1,lista2)  
eliminarEspacios(txt)
"""
listaVirus=[10, 11, 30]
indice=int(input("Digite el indice a buscar: "))
buscarVirus(listaVirus, indice)
