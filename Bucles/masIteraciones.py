#Creando las listas.
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = 'Hola Ramiro'
numeros = [2,4,6,8,10]

#Evitando que se coma una granada con la sentencia continue.
for fruta in frutas:
    if (fruta == 'granada'): #Desaparece granada ya que no la toma en cuenta.
        continue
    print(f'Me voy a comer una {fruta}')
    


#Evitar que el bucle siga ejecutandose   
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if (fruta == 'pera'):
        break #Con el break se saltea todo y el else tampoco lo ejecuta.
else:
    print('Bucle terminado')
    
    
#Recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
    
#For en una sola linea de codigo. (Duplicamos los numeros)
numerosDuplicados = [x * 2 for x in numeros]
print(numerosDuplicados)