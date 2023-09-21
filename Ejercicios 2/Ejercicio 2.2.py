#Creando una funcion que nos devuelva los numeros primos.
#Entre 0 y el argumento que pasamos.

#Crear una funcion que verifique si un numero es primo.
def esPrimo(num):
    #Verificamos que el numero pasado no pueda dividirse
    #Por ningun numero entero 2 y ese mismo numero - 1.
    for i in range(2,num - 1):
        #Si es divisible por alguno retornamos false y termina el bucle.
        if (num % i) == 0: return False
    #Si termina el bucle,significa que no fue divisible entonces es primo.
    return True


#Creando una funcion que retorne una lista con todos los primos.
def primosHasta(num):
    #Creamos la lista.
    primos = []
    for i in range(3, num + 1):
        #Verificamos si el valor es primo.
        resultado = esPrimo(i)
        #En caso de que sea lo agregamos a la lista.
        if(resultado == True): primos.append(i)
    #Devolvemos la lista.
    return primos

#Creamos el resultado llamando a la funcion y lo mostramos.
resultado = primosHasta(7)  #7 es numero primo asi que nos retorna True.
print(resultado)


primos_Hasta = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(2,num)))

print(primos_Hasta(7))
        
            
            