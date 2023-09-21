cadena1 = 'Hola soy Ramiro'
cadena2 = 'Bienvenido Ramiro'

print(dir(cadena1))  #Devuelve la lista de atributos validos del objeto pasado.Cada tipo de dato tiene diferentes atributos.

mayusc = cadena1.upper()   #Metodo de esta cadena => Convierte la cadena a mayusculas.

minusc = cadena1.lower()   #Metodo de esta cadena => Convierte la cadena a minusculas.

primeraLetraMayus = cadena1.capitalize() #Metodo de esta cadena => Convierte primero todo a minuscula y despues convierte la primera letra a mayuscula.

busquedaFind = cadena1.find('Hola') #Me devuelve 0 porque me devuelve la posicion en donde encuentra lo que le pedimos,sino encuentra un valor,nos devuelve -1.

busquedaIndex = cadena1.index('Hola') ##Me devuelve 0 porque me devuelve la posicion en donde encuentra lo que le pedimos,sino encuentra un valor,nos devuelve una exception.

esNumerico = cadena1.isnumeric() #Si es numerico devuelve true,sino devuelve false.

alfaNumerico = cadena1.isalpha() #Si es alfanumerico devuelve true,sino devuelve false. LETRAS DE LA A-Z. Los espacios no son caracteres alfanumericos.

contarCoincidencias = cadena1.count('a') #Devuelve la cantidad de coincidencias.

contarCaracteres = len(cadena1) #Contar cuantos caracteres tiene una cadena.

empiezaCon = cadena1.startswith('H') #Verifica si una cadena empieza con lo que le pasamos, si es asi devuelve true.

terminaCon = cadena1.endswith('H') #Verifica si una cadena termina con lo que le pasamos, si es asi devuelve true.

nuevaCadena = cadena1.replace('Ramiro', 'Andino') #Reemplaza un pedazo de la cadena dada,y la actualiza con lo que le pasemos.Si no encuentra coincidencia deja la misma cadena original.

separarCadena = cadena1.split(',') #Separa cadenas con la cadena que le pasamos.

print(mayusc)
print(minusc)
print(primeraLetraMayus)
print(busquedaFind)
print(busquedaIndex)
print(esNumerico)
print(alfaNumerico)
print(contarCoincidencias)
print(contarCaracteres)
print(empiezaCon)
print(terminaCon)
print(nuevaCadena)
print(separarCadena)