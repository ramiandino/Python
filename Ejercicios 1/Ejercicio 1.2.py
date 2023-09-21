#Le pedimos al usuario que nos diga una frase (o varias)
frase = input('Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ')

#Creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabrasSeparadas  = frase.split(' ')

#Usamos len() para ver la cantidad de elementos que hay en la lista.
cantidadDePalabras = len(palabrasSeparadas)

#En caso de que tarde mas de un minuto en decirlo, le decimos que pare un poco.
if (cantidadDePalabras > 120) : 
    print('Para flaco, tampoco te pedi un testamento')

#Calculamos cuanto tardaria en decir las palabras y se lo decimos.
print(f'Dijiste {cantidadDePalabras} palabras, y tardarias {cantidadDePalabras / 2} segundos en decirlo')
print(f'Dalto lo diria en {cantidadDePalabras * 100 // 2 * 1.3 / 100} segundos')