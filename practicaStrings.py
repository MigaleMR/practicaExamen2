################################################################################
#Elaborador por: Miguel Alejandro Madrigal Ramírez
#Fecha de creación: 28/09/2023, 11:40 pm
#Última modificación:
#Versión: 3.11.5
################################################################################
#Importación de librerías
import random
import time
from datetime import date
#Definición de funciones con strings 
#1. Convertir un número binario a decimal
def convertirBinarioDecimal(string):
    """
    Función: Convierte un número binario a decimal.
    Entradas: Un string con un número binario.
    Salidas: Un entero con el número decimal.
    """
    decimal = 0
    for i in range(len(string)):
        decimal += int(string[i]) * 2 ** (len(string) - 1 - i)
    return print(decimal)
"""string = input("Ingrese un número binario: ")
convertirBinarioDecimal(string)"""
#2. Calcular edad
def obtenerFecha():
    hoy= date.today()
    return str(hoy)
"print(obtenerFecha())"
def calcularEdad(fecha, hoy):
    """
    Función: Calcula la edad de una persona.
    Entradas: Un string con la fecha de nacimiento de la persona.
    Salidas: Un entero con la edad de la persona.
    """
    fecha = fecha.split("-")
    hoy = hoy.split("-")
    edad = int(hoy[0]) - int(fecha[0])
    if int(hoy[1]) < int(fecha[1]):
        edad -= 1
    elif int(hoy[1]) == int(fecha[1]):
        if int(hoy[2]) < int(fecha[2]):
            edad -= 1
    return edad
"""print(calcularEdad("2002-12-28", obtenerFecha()))"""
#3. Invertir Palabra
def invertirPalabraTerminadaenVocal(palabra):
    """
    Función: Invierte una palabra que termina en vocal.
    Entradas: Un string con la palabra a invertir.
    Salidas: Un string con la palabra invertida.
    """
    if palabra[-1] == "a" or palabra[-1] == "e" or palabra[-1] == "i" or palabra[-1] == "o" or palabra[-1] == "u":
        palabra = palabra[::-1]
        return print(palabra)
    else:
        return print("La palabra no termina en vocal.")
    
"""palabra=input("Ingrese una palabra: ")
print(invertirPalabraTerminadaenVocal(palabra))"""
#4. Dirección IP
def decirDireccionIP(ip):
    """
    Función: Dice si una dirección IP es válida o no.
    Entradas: Un string con la dirección IP.
    Salidas: Un string con un mensaje.
    """
    ip = ip.split(".")
    if len(ip) == 4:
        for i in range(len(ip)):
            if int(ip[0]) >9 and int(ip[0]) < 128:
                return print("La clase de la dirección IP es A.")
            elif int(ip[0])>128 and int(ip[0]) < 192:
                return print("La clase de la dirección IP es B.")
            elif int(ip[0])>191 and int(ip[0]) < 224:
                return print("La clase de la dirección IP es C.")
        return print("La dirección IP es válida.")
    else:
        return print("La dirección IP no es válida.")
"""   
ip = input("Ingrese una dirección IP: ")
decirDireccionIP(ip)"""

#5. Dime tu fecha de nacimiento y te dire como eres
def esBisiesto(anno):
    """
    Función: Dice si un año es bisiesto o no.
    Entradas: Un string con la fecha de nacimiento.
    Salidas: Un booleano.
    """

    if int(anno) % 4 == 0 and int(anno) % 100 != 0 or int(anno) % 400 == 0:
        return print("Bisiesto")
    else:
        return print("No bisiesto")
def esPar(dia):
    """
    Función: Dice si un número es par o no.
    Entradas: Un string con el día de nacimiento.
    Salidas: Un booleano.
    """
    if int(dia) % 2 == 0:
        return print("Par")
    else:
        return print("Impar")
def nombreMes(mes):
    """
    Función: Dice el nombre del mes.
    Entradas: Un string con el mes de nacimiento.
    Salidas: Un string con el nombre del mes.
    """
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    mesNumero = int(mes)
    
    if mesNumero >= 1 and mesNumero <= 12:
        return print(meses[mesNumero - 1])
    else:
        return "Mes no válido"
def signoZodiacal(dia, mes):
    """
    Función: Devuelve el signo zodiacal correspondiente al día y el mes.
    Entradas: Dos enteros, dia (1-31) y mes (1-12).
    Salidas: Un string con el signo zodiacal.
    """
    signos = ["Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]
    fechasInicio = [20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22]
    for i in range(11):
        if (mes == i + 1 and dia >= fechasInicio[i]) or (mes == (i % 12 + 1) and dia <= fechasInicio[i]):
            return print(signos[i])
    return print(signos[11])

def personalidad(fecha,nombre):
    """
    """
    dia=int(fecha[0:2])
    mes=int(fecha[3:5])
    anno=int(fecha[6:10])   
    diaNacimiento = esPar(dia)
    mesNacimiento = nombreMes(mes)
    annoNacimiento = esBisiesto(anno)
    signo = signoZodiacal(dia,mes)
    resultado = f"Usted, {nombre}, nació en un día {diaNacimiento} del mes {mesNacimiento} del año {annoNacimiento}, por lo tanto su signo zodiacal es {signo}"
    return print(resultado) 
fecha = input("Ingrese su fecha de nacimiento: ")
nombre = input("Ingrese su nombre: ")
personalidad(fecha,nombre)