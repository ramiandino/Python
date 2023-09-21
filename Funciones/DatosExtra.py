#Creando una funcion de 3 parametros.

def frase (nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido} sos muy {adjetivo}'

#Utilizando keyword arguments

fraseResultante = frase(adjetivo = 'capo', nombre = 'Ramiro', apellido = 'Andino',)
print(fraseResultante)


#Creando la misma funcion con un parametro opcional y un valor por defecto. valor por defecto es capo y el opcional inteligente.
def frase2 (nombre,apellido,adjetivo = 'capo'):
    return f'Hola {nombre} {apellido} sos muy {adjetivo}'
fraseResultante2 = frase2(nombre = 'Ramiro', apellido = 'Andino', adjetivo = 'inteligente')  
print(fraseResultante2)

