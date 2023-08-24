import math

#1. Escribir una función que calcule el máximo común divisor entre dos números.

def maximo_comun_denominador(numero_uno, numero_dos):
    return math.gcd(numero_uno, numero_dos)

#2. Escribir una función que calcule el mínimo común múltiplo entre dos números
def minimo_comun_multiplo(numero_uno, numero_dos):
    return math.lcm(numero_uno, numero_dos)

#3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
#cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def cant_palabras(frase):
    return frase.count(' ') + 1 

#4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
#palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
#que reciba el diccionario generado con la función anterior y devuelva una tupla con la
#palabra más repetida y su frecuencia.

def guardar_palabra_diccionario(frase):
    palabras = frase.split()#divide la cadena en palabras
    apariciones = {}#guardo la palabra y su cantidad de apariciones
    for palabra in palabras:
        palabra = palabra.lower()#paso toda la palabra a minuscula para poder compararlas sin problemas por el uso de mayusculas y minusculas
        if palabra in apariciones:
            apariciones[palabra] += 1
        else:
            apariciones[palabra] = 1
    return apariciones

def palabra_mas_repetida (apariciones):
    mas_repetida = None
    maximo_apariciones = 0
    
    for palabra, apariciones in apariciones.items():
        if apariciones > maximo_apariciones:
            mas_repetida = palabra
            maximo_apariciones = apariciones
    
    return (mas_repetida, maximo_apariciones)


numero_uno = int(input("Ingrese un numero: "))
numero_dos = int(input("Ingrese otro numero: "))
frase = input("Introduce una frase: ")

max_com_deno = maximo_comun_denominador(numero_uno, numero_dos)
min_com_mult = minimo_comun_multiplo(numero_uno, numero_dos)
cant_pala = cant_palabras(frase)
diccionario_palabras = guardar_palabra_diccionario(frase)
palabra_mas_usada , frecuencia = palabra_mas_repetida(frase)#asi lo guardo en una tupla

print(f'El maximo comun denominador entre {numero_uno} y {numero_dos} es {max_com_deno}.')
print(f'El minimo comun multiplo entre {numero_uno} y {numero_dos} es {min_com_mult}.')
print(f'{frase} tiene {cant_pala} palabras')
print("Frecuencia de palabras:")
for palabra, frec in diccionario_palabras.items():
    print(f"{palabra}: {frec}")
print(f'La palabra mas repetida: {palabra_mas_usada} {frecuencia}')