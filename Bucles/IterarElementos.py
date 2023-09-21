animales = ["gato","perro","loro","cocodrilo"]
numeros =[52,16,32,44]

#Recorriendo la lista animales.
for animal in animales :
    print(animal)
    
#Recorriendo la lista numeros y multiplicando cada valor por 10.
for numero in numeros :
    resultado = numero * 10
    print(resultado)
  
#Recorriendo las 2 listas al mismo tiempo.  
for numero,animal in zip(animales,numeros) :
    print(f'Recorriendo lista 1: {numero}')
    print(f'Recorriendo lista 2: {animal}')


#Forma no optima de recorrer una lista (no funciona en conjuntos).
for num in range(len(numeros)) :
    print(numeros[num])
    
#Forma correcta de recorrer una lista con su indice.
for num in enumerate(numeros) :
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y el valor es: {valor}')
    
#Usando el else
for numero in numeros:
    print(f'Ejecutando el ultimo bucle,valor actual: {numero}')
else:
    print('El bucle termino')
    
#Todo lo anterior funciona exactamene igual para tuplas y conjuntos.