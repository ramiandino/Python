#Usando open para abrir un archivo con una codificacion universal (utf-8)
archivo = open("archivos\\textoDeRami.txt",encoding='utf-8') #UTF-8 para que lea todos los caracteres.
#Leer archivo completo
print(archivo.read())  #Read para leer el archivo.

lineas = archivo.readlines()
#Leer linea por linea
print(lineas)

#Leer una sola linea
linea = archivo.readline()
print(linea)

#Cerrar el archivo

archivo.close()