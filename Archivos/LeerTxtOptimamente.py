#Abriendo el archivo con with open
with open("Archivos\\textoDeRami.txt",encoding='utf-8') as archivo:
    #Leemos el archivo
    contenido = archivo.read()
    #Mostramos el archivo
    print(contenido)
    
#Se abrio el archivo,se ejecuto el codigo y se cerro.
#No es necesario cerrar el archivo al usar with open.
#Menos errores de exceptions y mas optimo.