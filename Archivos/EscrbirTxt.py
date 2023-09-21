with open('archivos\\textoDeRami.txt','w',encoding='utf-8') as archivo:
    #Sobreescribiendo el archivo
    # archivo.write('JAJAJAAJ')
    
    #Agregando 2 lineas con writelines
    archivo.writelines(['Hola maestro\n','como andas?\n'])
    
    #Agregando otras 2 lineas
    archivo.writelines(['Hola maestro\n','como andas?\n'])
    
    
    