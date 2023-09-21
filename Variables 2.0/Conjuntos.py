#Creando un conjunto con set()
conjunto = set(["Ramiro", "Andino"])

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(['dato1', 'dato2'])
conjunto2 = {conjunto1,'dato3'}

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

resultado = conjunto2.issubset(conjunto1) #conjunto2 es un subconjunto de conjunto1.
resultado = conjunto2 <= conjunto1 #Es lo mismo que arriba.

resultado = conjunto2.issuperset(conjunto1) #conjunto2 no es un superconjunto de conjunto1.
resultado = conjunto2 > conjunto1 #Es lo mismo que arriba.

#Verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)  #Va a ser True solo si los 2 conjuntos tienen numeros distintos.

print(conjunto2)
print(resultado)