diccionario = {
    "nombre" : "Ramiro",
    "apellido" : "Andino",
    "edad" : "23"
}

clave1 = diccionario.keys() #Devuelve las claves y tambien nos sirve para iterar.

clave2 = diccionario.get("nombre") #Obtiene un elemento,no me lanza una exception y si no encuentra nada el programa continua.

diccionario.pop("nombre") #Elimina un elemento del diccionario.Si quiero eliminar mas elementos con la , puedo agregar mas.

diccionarioIterable = diccionario.items() #Recorriendo los elementos.Obtiene un elemento iterable.

diccionario.clear() #Elimina todos los elementos del diccionario.

print(clave1)
print(clave2)
print(diccionarioIterable)