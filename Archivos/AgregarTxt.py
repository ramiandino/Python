with open('archivos\\textoDeRami.txt','a',encoding='utf-8') as archivo:
    #Agregando el archivo
    #Usando un bucle para agregar varias lineas.
    archivo.write('\n')
    for i in range(5):
        #Agregando lineas.
        archivo.write(f'Linea {i+1} agregada\n')
   
    
    
    