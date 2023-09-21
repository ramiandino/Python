#Falto el profe y los pibes van a armar la clase.

#Pedir el nombre y la edad de los compañeros que vinieron hoy a clase.

#Funcion para obtener al asistente y profesor segun la edad.
def obtenerCompañeros(cantCompañeros):
    #Creando la lista con los compañeros.
    compañeros = []
    #Ejecutando un for para pedir informacion de cada compañero
    for i in range(cantCompañeros):
        nombre = input('Ingrese el nombre del compañero: ')
        edad = int(input('Ingrese la edad del compañero: '))
        compañero = (nombre,edad)
        #Agregando informacion a la lista.
        compañeros.append(compañero)
    #Ordenarlos de menor a mayor segun su edad.
    compañeros.sort(key = lambda x : x[1])   #Ordena la edad de mayor a menor, pos 1 porque la edad es el 2do parametro.
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre.
    #Para definir al asistente y profesor.
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    #Retornamos una tupla.
    return asistente, profesor
#Desempaquetamos lo que nos retorna la funcion.
asistente,profesor = obtenerCompañeros(5)
#Mostrando el resultado.
print(f'El profesor es {profesor} y su asistente es {asistente}')
