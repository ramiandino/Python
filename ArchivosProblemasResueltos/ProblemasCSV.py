#Cambiar el tipo de dato de una columna.
import pandas as pd
df = pd.read_csv("Archivos\\datos.csv")

#Convertir a string los datos de una columna
df['edad'] = df['edad']. astype(str)

#Mostrar el tipo de dato del primer elemento de la columna edad.
print(type(df['edad'][0]))

#Reemplazando Ramiro por Tomas
df['nombre'].replace("Ramiro","Tomas",inplace=True)
print(df['nombre'])


#Eliminando las filas con datos vacios.
df = df.dropna()
print(df)

#Eliminando las filas repetidas.

df = df.drop_duplicates()
print(df)

#Creando un CSV con el dataframe resultante (limpio)

df.to_csv("ArchivosProblemasResueltos\\datos_limpios.csv")