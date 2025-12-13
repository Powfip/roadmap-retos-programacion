#EJEMPLOS DE TIPOS DE OPERADORES EN PYTHON
#OPERADORES ARITMÉTICOS 
valor_1 = 5
valor_2 = 5
print(valor_1 + valor_2) #Suma
print(valor_1 - valor_2) #Resta
print(valor_1 * valor_2) #Multiplica
print(valor_1 / valor_2) #Division
print(valor_1 // valor_2) #Division entera
print(valor_1 % valor_2) #Resto de la division
print(valor_1 ** valor_2) #Potencia

#OPERADORES BIT A BIT 
print(valor_1 & valor_2) # AND
print(valor_1 | valor_2) # OR
print(valor_1 ^ valor_2) # XOR
print(~valor_1) # NOT
print(valor_1 << 2) # DESPLAZAMIENTO HACIA LA IZQUIERDA
print(valor_1 >> 2) # DESPLAZAMIENTO HACIA LA DERECHA


#OPERADORES DE COMPARACION

print(valor_1 == valor_2) # OPERADOR DE IGUALDAD
print(valor_1 <= valor_2) # OPERADOR DE MENOR/IGUAL QUE
print(valor_1 >= valor_2) # OPERADOR DE MAYOR/IGUAL QUE
print(valor_1 < valor_2) # OPERADOR DE MENOR QUE
print(valor_1 > valor_2) # OPERADOR DE MAYOR QUE
print(valor_1 != valor_2) # OPERADOR DE DIFERENTE QUE

# OPERADORES DE ASIGNACIÓN  
num1 = 10
num1 += 1 # num1 = num1 + 1
print(num1) 
num1 -= 1 # num1 = num1 - 1
print(num1)
num1 *= 2 # num1 = num1 * 2
print(num1)
num1 **= 2 # num1 = num1 ** 2
print(num1)
num1 /= 2 # num1 = num1 / 2
print(num1)
num1 //= 2 # num1 = num1 // 2
print(num1)
num1 %= 2 # num1 = num1 % 2
print(num1)

# OPERADORES LÓGICOS

if valor_1 < 10 and valor_2 > 2:
    print("La condicion se cumple")
if valor_1 < 10 or valor_2 <= 5:
    print("La condicion se cumple.")
if not valor_2 > 5:
    print("La condicion se cumple")

# OPERACIONES DE PERTENENCIA

lista = [1,2,3,4,5]

if 5 in lista:
    print("True")
if 10 not in lista:
    print("True")

# OPERADORES DE IDENTIDAD
number_1 = 5
number_2 = 5
number_3 = 2

print(number_1 is number_2)
print(number_1 is not number_2)
print(number_1 is not number_3)

# ESTRUCTURA DE CONTROL CONDICIONAL

mi_variable = 4

if mi_variable > 10:
    print("La variable es mayor que 10")
elif mi_variable < 10:
    print("La variable es menor que 10.")
else:
    print("La variable es igual a 10.")       

# ESTRUCTURA DE CONTROL ITERATIVA

for i in "GINECOMASTIA":
    print(i)

mi_variable = 5
while mi_variable < 10:
    print(mi_variable)
    mi_variable += 1

# ESTRUCTURA DE CONTROL DE EXCEPCIONES

try:
    print(15/0)
except ZeroDivisionError:
    print("Error. No se puede dividir por cero.")
finally:
    print("Se termina la ejecución.")

# DIFICULDAD EXTRA

def numeros():
    for i in range(10,56):
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            print(i)
numeros()