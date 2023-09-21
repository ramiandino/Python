import pandas as pd

#Usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("archivos\\datos.csv")         # names = ["name","lastname","age"]
df2 = pd.read_csv("archivos\\datos.csv") 
print(df)

#Obteniendo los datos de la columna nombre.
nombres = df["nombre"]

cadena = '0123456789'

print(cadena[:])    #Si lo dejamos asi,arranca en el primer elemento y termina en el ultimo

print(cadena[:3])  #Aca daria => 0,1,2


#Ordenamos dataframe por la edad.
# df_orden_ascendente = df.sort_values("edad")

#Ordenando de forma descendente
# df_orden_descendente = df.sort_values("edad",ascending=False)

# print(df_orden_ascendente)
# print(df_orden_descendente)

#Concatenando los 2 dataframes.
df_concatenado = pd.concat([df,df2])

print(df_concatenado)

#Accediendo a la primeras 3 filas con head()

primerFila = df.head(3)

print(primerFila)

#Accediendo a las ultimas 3 filas con tail()

ultimasFilas = df.tail(3)

print(ultimasFilas)

#Accediendo a la cantidad de filas y columnas con shape.

filasTotales,columnasTotales = df.shape

print(filasTotales)
print(columnasTotales)

#Obteniendo data estadistica del dataframe:

df_info = df.describe()
print(df_info)

#Accediendo a un elemento especifico del df con loc

elementoEspecificoLoc = df.loc[2,"nombre"]

print(elementoEspecificoLoc)

#Accediendo a un elemento especifico del df con iloc

elementoEspecificoILoc = df.iloc[2,1]

print(elementoEspecificoLoc)
print(elementoEspecificoILoc)

#Accediendo a todas las filas de una columna

apellidosIloc = df.iloc[:,1]
print(apellidosIloc)

apellidosloc = df.loc[:"apellido"]
print(apellidosloc)

#Accediendo a la fila 3 con loc

fila3Loc = df.loc[2,:] 
print(fila3Loc)

#Accediendo a la fila 3 con iloc

fila3Iloc = df.iloc[2,:] 
print(fila3Iloc)




