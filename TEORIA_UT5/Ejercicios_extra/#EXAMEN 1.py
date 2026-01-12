#EXAMEN 1
#Ejercicio 2 - Lista de prefijos telefónicos
#Escribir un programa que contenga un diccionario con la lista de prefijos telefónicos de países y que tenga una función que permita chqeuear e identificar si un número de teléfono está bien escrito y a qué país corresponde su prefijo. Deberá serpara el número del prefijo y comprobar si el número es correcto y a que país corresponde el prefijo.
#Lo primero es crear el diccionario con los prefijos telefónicos de los suiguientes países:Grecia, Francia, España, Portugal, Ucrania, Italia, Suiza, Reino Unido, Almenaia y Rusia.

prefijos_telefonicos = {
    "Grecia": "+30",   
    "Francia": "+33",
    "España": "+34",
    "Portugal": "+351",
    "Ucrania": "+380",
    "Italia": "+39",
    "Suiza": "+41",
    "Reino Unido": "+44",
    "Alemania": "+49",
    "Rusia": "+7"
}

#Crear funcion para chequear el número de teléfono, a la cual se le pasará como parámetro el número de teléfono separado del prefijo y deberá compprobar si es correcto, es decir, que contiene 9 dígitos y empieza por 6. Esta función devolverá un boolenao false si el número es incorrecto y un booleano True si el número es correcto.
def chequear_numero(numero):
    if len(numero) == 9 and numero.startswith("6") and numero.isdigit():
        return True
    else:
        return False
    
#Repite la función anterior utilizando expresión regular.
import re
def chequear_numero_regex(numero):
    patron = r"^6\d{8}$"
    if re.match(patron, numero):
        return True
    else:
        return False
    

#No lo puedes hacer comprobando cada carácter por separado? comprueba primero el primer carácter y luego la longitud total y si son dígitos.
def chequear_numero_manual(numero):
    if len(numero) != 9:
        return False
    if numero[0] != '6':
        return False
    for char in numero:
        if not char.isdigit():
            return False
    return True

#Crear una función que compruebe el prefijo en el diccionario.
#Cómo parámetro de entrada, recibirá un str que será el prefijo telefónico en el formato de símbolo + seguido del número.
#Ejemplo: "+34 "
#Cómo retorno, devolverá un str que será el nombre del país si lo encuentra en el diccionario o None si no lo encuentra.

def comprobar_prefijo(prefijo):
    for clave, valor in prefijos_telefonicos.items():
        if valor == prefijo:
            return clave
    return None

#Crear función que reciba como parámetro un número completo y separe el número en dos partes, prefijo y número de teléfono.
#Como parámetro de entrada recibirá el número de teléfono completo de la siguiente forma: +34-612345678 dónde +34 es el prefijo y 612345678 es el número de teléfono.
#La función deberá separar el prefijo del número y comprobar si el prefijo existe en el diccionario y si el número es correcto utilizando las funciones anteriores.

def identificar_numero_completo(numero_completo):
    try:
        prefijo, numero = numero_completo.split("-")
    except ValueError:
        return "número incorrecto"
    
    pais = comprobar_prefijo(prefijo)
    
    if pais and chequear_numero(numero):
        return f"llamando a {numero} de {pais}"
    else:
        return "número incorrecto"

   
#Programa principal
numero = input("Introduce un número de teléfono completo (formato +XX-XXXXXXXXX): ")
resultado = identificar_numero_completo(numero)
print(resultado)
opcion = input("¿Desea comprobar otro número? (s/n): ")
while opcion.lower() == 's':
    numero = input("Introduce un número de teléfono completo (formato +XX-XXXXXXXXX): ")
    resultado = identificar_numero_completo(numero)
    print(resultado)
    opcion = input("¿Desea comprobar otro número? (s/n): ")
print("Programa finalizado.")
