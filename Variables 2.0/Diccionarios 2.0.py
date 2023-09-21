#Creando diccionario con dict()

diccionario = dict(nombre="Ramiro", apellido="Andino")

#Las listas no pueden ser claves porque son iterables y usamos frozenset para meter conjuntos.

diccionario = {frozenset(["Ramiro","Andino"]):"23"}

#Creando un diccionario con fromkeys()

diccionario = dict.fromkeys(["nombre","apellido"]) #Valor por defecto None.

#Creando diccionarios con fromkeys() cambiando el valor por defecto a "No se"

diccionario = dict.fromkeys(["nombre","apellido"],"No se")

print(diccionario)