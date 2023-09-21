numeros = [4,7,1,42,15]

#Encontrando el numero mayor en una lista.

numeroMayor = max(numeros)

print(numeroMayor)

#Encontrando el numero menor en una lista.

numeroMenor = min(numeros)

print(numeroMenor)

#Redondeando a 6 decimales.

numero = round(12.345678,2)   #El 2do parametro es cuantos decimales queremos que tenga el numero.

print(numero)

#Retorna False => 0, vacio, False, None
#Retorna True => Distinto de 0, True, Cadena, Datos no vacios

resultadoBool = bool(1)

print(resultadoBool)

#Retorna True si todos los valores son verdaderos.

resultadoAll = all([234,"true",[344,23]])

print(resultadoAll)

#Suma todos los valores de un iterable.

sumaTotal = sum(numeros)

print(sumaTotal)