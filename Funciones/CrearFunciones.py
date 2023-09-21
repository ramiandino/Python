#Creando una funcion simple.

def saludar ():
    print('Hola Ramiro, como andas?')

#Ejecutando la funcion simple.  
saludar()

#Crear una funcion con parametros.

def saludar(nombre,sexo):
    sexo = sexo.lower()
    if(sexo == 'mujer'):
        adjetivo = 'reina'
    elif(sexo == 'hombre'):
        adjetivo = 'rey'
    else:
        adjetivo = 'amor'
    print(f'Hola {nombre}, mi {adjetivo} ¿Como andas?')
    
saludar('Ramiro','hombre')

#Crear una funcion que nos retorne multiples valores

def crearContraseñaRandom(num):
    chars = 'abcdefghij'
    numEntero = str(num)
    num = int(numEntero[0])
    caracter1 = num - 2
    caracter2 = num
    caracter3 = num - 5
    contraseña = f'{chars[caracter1]}{chars[caracter2]}{chars[caracter3]}{num * 2}'
    return contraseña,num

#Desempaquetando la funcion    
password,primerNumero = crearContraseñaRandom(981)

#Mostrando los resultados obtenidos y los datos utilizados para obtenerlo.
print(f'Tu contraseña nueva es: {password}')
print(f'El numero utilizado para crearla fue: {primerNumero}')
#return nos permite que el dato poder guardarlo,si nosotros usamos print no podemos hacer nada con el dato.