numeros = [1,2,3,4,5,6,7,8,9]

#Creando una funcion lambda

multiplicarPorDos = lambda x : x * 2

print(multiplicarPorDos(5))

#Creando una funcion comun que diga si es par o no

def esPar (num): 
    if (num % 2 == 0):
        return True


#Usando filter con una funcion comun

numerosPares = filter(esPar,numeros)

print(list(numerosPares))  #Me filtra los numeros pares.


#Creando lo mismo que antes pero con lambda.

numerosParesLambda = filter(lambda numero : numero % 2 == 0,numeros)

print(list(numerosParesLambda))

