#Forma no optima de sumar valores.

def suma (lista):
    numerosSumados = 0
    for numero in lista:
        numerosSumados = numerosSumados + numero
    return numerosSumados
resultado = suma([5,3,2,5,6,7,8,4])

print(resultado)

#-------------------#

#Forma optima de sumar valores.

def sumaTotal (numeros):
    return sum([*numeros])
resultado2 = sumaTotal([5,3,2,5,6,7,8,4])

print(resultado2)

#-------------------#


#Utilizando el parametro args => Forma optima.
#Utilizar el operador * como argumento (*args)

def suma(nombre,*numeros):
    return f'{nombre}, la suma de tus numeros es: {sum(numeros)}'
resultado = suma('Ramiro',5,3,2,5,6,7,8,4)

print(resultado)