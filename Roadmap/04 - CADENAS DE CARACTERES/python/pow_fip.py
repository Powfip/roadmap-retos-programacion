# #04 CADENAS DE CARACTERES
#### Dificultad: Media | Publicación: 22/01/24 | Corrección: 29/01/24

## Ejercicio

'''
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
'''
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

#Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

#> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.

# Encontrar posicion de caracteres
palabra = "Python"
print(palabra.find("a")) # Devuelve la posición de la primera aparición de la letra "a" en la cadena

# Reemplazar caracteres
print(palabra.replace("P", "J")) # Reemplaza "P" por "J" en la cadena

# Buscar subcadenas
print(palabra.find("a", 2)) # Devuelve la posicion de la segunda aparacion de la letra "a" en la cadena

# Contar ocurrencias de un caracter
print(palabra.count("a")) # Devuelve la cantidad de veces que aparece la letra "a" en la cadena

# Mayuscula la primera letra de la cadena
print(palabra.capitalize()) # Devuelve la cadena con la primera letra en mayusculas

# Verificar si es un numero
print(palabra.isdigit()) # Devuelve True si la cadena es un número

# Verificar si es una letra
print(palabra.isalpha()) # Devuelve True si la cadena es una letra

# Verificar si es alfanumérica
print(palabra.isalnum()) # Devuelve True si la cadena es alfanumérica

# verificar longitud de la cadena
print(len(palabra)) # Devuelve la longitud de la cadena

# verificar si la cadena es vacía
print(palabra.isspace()) # Devuelve True si la cadena es vacía

# Minusculas todas las letras de la cadena
print(palabra.lower()) # Devuelve la cadena en minusculas

# Mayusculas todas las letras de la cadena
print(palabra.upper()) # Devuelve la cadena en mayúsculas

# Verificar le caracter más largo de la cadena
print(max(palabra)) # Devuelve el caracter más largo de la cadena

# Verficar el caracter más corto de la cadena
print(min(palabra)) # Devuelve el caracter más corto de la cadena

# Dividir la cadena en una lsita de subcadenas
print(palabra.split()) # Devuelve una lista con las subcadenas de la cadena

# Concatenar dos cadenas
frase = "Es un lenguaje de programación"
print(f"{palabra} + {frase}") # Devuelve la concatenacion de las dos cadenas

# Repetir una cadena
print(palabra * 2) # Devuelve la cadena repetida dos veces

# Recorrer una cadena
for caracter in palabra:
    print(caracter) # Imprime cada caracter de la cadena

# Interpolar cadenas
print(f"{palabra} es un lenguaje de programación") # Devuelve la cadena interpolada

# Verificar si la cadena contiene una subcadena
print(palabra in frase) # Devuelve True si la cadena contiene la subcadena

# Verificar si la cadena comienza con una subcadena
print(palabra.startswith("Py")) # Devuelve True si la cadena comienza con la subcadena

# Verificar si la cadena termina con una subcadena
print(palabra.endswith("a")) # Devuelve True si la cadena termina con la subcadena

# Verificar si la cadena contiene una subcadena
print(palabra.index("a")) # Devuelve la posicion de la primera aparicion de la subcadena

# Verificar si la cadena es un palindromo
def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]
def verificar_palindromo(palabra1, palabra2):
    if es_palindromo(palabra1)  and es_palindromo(palabra2):
        print(f"{palabra1} y {palabra2} son palíndromos")
    elif es_palindromo(palabra1):
        print(f"{palabra1} es palíndromo pero {palabra2} NO lo es.")
    elif es_palindromo(palabra2):
        print(f"{palabra2} es palíndromo pero {palabra1} NO lo es.")
    else:
        print(f"{palabra1} y {palabra2} NO son palíndromos")
palabra1 = input("Introducir palabra: ")
palabra2 = input("Introducir palabra: ")
palindromo = verificar_palindromo(palabra1, palabra2)


# Verificar si la cadena es un anagrama
def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")

    # Verificar si las palabras tienen la misma cantidad de letras
    if len(palabra1) != len(palabra2):
        return False
    
    # Verificar si ambas palabras contienen las mismas letras
    return sorted(palabra1) == sorted(palabra2)

palabra1 = input("Introducir palabra: ")
palabra2= input("Introducir palabra: ")

if son_anagramas(palabra1, palabra2):
    print(f"{palabra1} y {palabra2} son anagramas")
else:
    print(f"{palabra1} y {palabra2} no son anagramas")


# Verificar si es una isograma
def es_isograma(palabra):
    palabra = palabra.lower().replace(" ", "")
    return len(set(palabra)) == len(palabra)

def verificar_isograma(p1,p2):
    return es_isograma(p1) and es_isograma(p2)
palabra1 = input("Introducir palabra: ")
palabra2 = input("Introducir palabra: ")

isograma1 = es_isograma(palabra1)
isograma2 = es_isograma(palabra2)

if isograma1 and isograma2:
    print(f"{palabra1} y {palabra2} son isogramas")
elif isograma1:
    print(f"{palabra1} es isograma pero {palabra2} NO lo es")
elif isograma2:
    print(f"{palabra2} es isograma pero {palabra1} NO lo es")
else:
    print(f"{palabra1} y {palabra2} NO son isogramas")