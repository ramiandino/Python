lista = list(["Hola", "soy", "Ramiro"])  #Crea una lista con list.

cantElementos = len(lista) #Nos devuelve la cantidad de elementos de la lista.

lista.append('23') #Agrega el elemento a la lista.

lista.insert(3, 'Edad:') #Agrega el elemento en la posicion especifica que le indiquemos.

lista.extend(['Sexo:', 'Masculino']) #Agrega varios elementos a la lista.

lista.pop(1) #Eliminar un elemento de la lista por su indice.Con -1 elimina el ultimo elemento de la lista.Con -2 elimina el anteultimo y asi sucesivamente.

lista.remove('Hola') #Remueve un elemento por su valor.Si no existe el valor,nos devuelve una exception.

lista.sort() #Ordena los elementos de forma ascendente.

lista.sort(reverse=True) #Ordena los elementos alrevez,de forma inversa.

lista.reverse() #Invierte los elementos de una lista.

lista.clear() #Elimina todos los elementos de la lista.

print(lista)
print(cantElementos)